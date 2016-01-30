from django.db import models
from django.conf import settings 

from django.contrib.auth.models import User
from django.db.models import Sum

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string

# Create your models here.

class Fgroup(models.Model):
    # Include in Admin
    # examples, English League, champions league 2017
    DEFAULT_PK=1
    group_name = models.CharField(max_length=200, help_text='Name of group, e.g. Champions League')

    def __str__(self):              # __unicode__ on Python 2
        return self.group_name

class Team(models.Model):
    # Include in Admin
    # The list of eligable teams, e.g. English football
    # Some team may drop out of the league  - tough luck
    fgroup = models.ForeignKey(Fgroup, on_delete=models.CASCADE, default=Fgroup.DEFAULT_PK)
    team_name = models.CharField(max_length=200, help_text='Name of Team')

    def __str__(self):              # __unicode__ on Python 2
        return self.team_name

    class Meta:
        ordering = ['id']


class Series(models.Model):
    # Include in Admin
    series_name = models.CharField(max_length=200, help_text='Name of series of games')
    series_open = models.BooleanField(default=True)
    entry_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rollover = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    end_message = models.TextField(null=True, blank=True, help_text="A Message to include at end of series (e.g. Winner: HHH, after 8 rounds")

    def __str__(self):              # __unicode__ on Python 2
        return self.series_name
    def paid(self):
        paid = Payment.objects.filter(series=self.id, paid=True)
        return paid
    def naughty(self):
        paid_users = Payment.objects.filter(series=self.id, paid=True).values('user')
        round_f = Round.objects.filter(series=self.id)
        naughty_users = Prediction.objects.filter(round_f=round_f).exclude(user=paid_users)
        return naughty_users
    def spectators(self):
        spectators = User.objects.exclude(id__in =self.paid().values_list('user')).exclude(id__in =self.naughty().values_list('user'))
        return spectators
    def expected_prize_pot(self):
        payment_total = self.paid().aggregate(Sum('payment')).get('payment__sum')
        return payment_total + self.rollover + (len(self.naughty()) * self.entry_cost)

    class Meta:
        ordering = ['-id']
  
class Round(models.Model):
    # Include in Admin
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    round_date = models.DateTimeField('Date games will be played on')
    round_open = models.BooleanField(default=True)
    email_message = models.TextField(null=True, blank=True, help_text="A Message to include in the email")

    def staff_predictions(self):
        p = Prediction.objects.filter(round_f=self.id).filter(user__is_staff=1)
        return p

    def __str__(self):              # __unicode__ on Python 2
        return self.series.series_name + " " + str(self.round_date)
    class Meta:
        ordering = ['-round_date']


class Emailround(models.Model):
    # Include in Admin in case of error.
    # Slowly notify users of new round. 
    # Cron job ?
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    sent = models.BooleanField(default=True)

class Payment(models.Model):
    # Include in Admin
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    payment = models.DecimalField(max_digits=5, decimal_places=2, default=5)
    class Meta:
        ordering = ['series']

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user) + " " + str(self.series) + " " + str(self.payment)

@receiver(post_save, sender=Payment, dispatch_uid="update_payment")
def update_payment(sender, instance, **kwargs):
    payment = instance
    message = "Payment received, £" + str(payment.payment) + ". You are now off the naughty step."
    c = Context({'message': message, 'user': payment.user,}) 
    text_content = render_to_string('email/payment.txt', c)
    subject = "NoNilNil - Payment received for " + str(payment.series)
    send_mail(subject, text_content, "NoNilNil Payments <no-reply@NoNilNil.com>", [payment.user.email], fail_silently=False)


class Prediction(models.Model):
    # User form - the only one ?
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user) + " " + str(self.round_f) + " " + str(self.team)
    def failed(self):
        possible_nilnils = Nilnils.objects.filter(round_f=self.round_f, team=self.team)[:1]
        if possible_nilnils:
            return(Nilnils.objects.get(round_f=self.round_f, team=self.team).ohno)
        else:
            return(False)
    class Meta:
        ordering = ['round_f']


class Nilnils(models.Model):
    # Superuser form, list teams select from that round and edit the ohno by exception
    round_f = models.ForeignKey(Round, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False)
    ohno = models.BooleanField(default=False)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.round_f) + " " + str(self.team) + " " + str(self.ohno)
    class Meta:
        ordering = ['round_f']


class Medal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    MEDALS_CHOICES = (
        ('Gold', 'Gold - Winning a series'),
        ('Silver', 'Silver - Comming 2nd'),
        ('Bronze', 'Bronze - 3rd in a series'),
        ('90', '90 - Goal in times added on (not extra time) to avoid nil nil'),
        ('TopGoal', 'TopGoal - Picked the game out of all the possible games with the highest number of goals'),
        ('AFC', 'AFC - Picked AFC Wimbledon in a game they won'),
        ('Bomb', 'Bomb - Out in the first week'),
        ('Warning', 'Warning - Lost because of a rule volalation'),
        ('Postpone', 'Postpone - Lost becasue of a postponed game'),
        ('Twitter', 'Twitter - Followed @NoNilNil on twitter'),
        ('Group', 'Group - Introduced NoNilNil, to someone outside of TI'),
        ('Globe', 'Globe - Introduced NoNilNil, to someone outside of the UK'),
    )
    tag = models.CharField(null=True, blank=True, max_length=10,
                                      choices=MEDALS_CHOICES)
    medal_date = models.DateField('Date games will be played on')
    description = models.TextField('Glory description')

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user) + ": " + str(self.tag)
    class Meta:
        ordering = ['medal_date']


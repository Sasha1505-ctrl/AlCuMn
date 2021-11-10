from django.db import models


class Message(models.Model):
    username = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


class Discipline(models.Model):
    numdiscipline = models.AutoField(db_column='NumDiscipline', primary_key=True)  # Field name made lowercase.
    namediscipline = models.TextField(db_column='NameDiscipline')  # Field name made lowercase.
    idteacher = models.ForeignKey('User', models.DO_NOTHING, db_column='IDTeacher')  # Field name made lowercase.

    def __str__(self):
        return f'{self.namediscipline}'


class Lesson(models.Model):
    idlesson = models.AutoField(db_column='IDLesson', primary_key=True)  # Field name made lowercase.
    descriplesson = models.TextField(db_column='DescripLesson', blank=True, null=True)  # Field name made lowercase.
    datestart = models.DateTimeField(db_column='DateStart')  # Field name made lowercase.
    deadline = models.DateTimeField(db_column='DeadLine', blank=True, null=True)  # Field name made lowercase.
    typelesson = models.TextField(db_column='TypeLesson')  # Field name made lowercase. This field type is a guess.
    availabhomework = models.BinaryField(db_column='AvailabHomework')  # Field name made lowercase.
    group = models.TextField(db_column='Group', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    textpractice = models.TextField(db_column='TextPractice', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    numdiscipline = models.OneToOneField('Discipline', models.DO_NOTHING,
                                         db_column='NumDiscipline')  # Field name made lowercase


class User(models.Model):
    iduser = models.AutoField(db_column='IDUser', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    family = models.TextField(db_column='Family')  # Field name made lowercase. This field type is a guess.
    group = models.TextField(db_column='Group', blank=True,
                             null=True)  # Field name made lowercase. This field type is a guess.
    birthdate = models.DateField(db_column='BirthDate')  # Field name made lowercase.
    mail = models.TextField(db_column='Mail', unique=True, blank=True,
                            null=True)  # Field name made lowercase. This field type is a guess.
    password = models.TextField(db_column='Password')  # Field name made lowercase. This field type is a guess.
    usertype = models.TextField(db_column='UserType', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.


class Certificate(models.Model):
    numcertificate = models.AutoField(db_column='NumCertificate', primary_key=True)  # Field name made lowercase.
    namecertificate = models.TextField(
        db_column='NameCertificate')  # Field name made lowercase. This field type is a guess.
    datecertificate = models.DateField(db_column='DateCertificate')  # Field name made lowercase.
    issuedwhom = models.TextField(db_column='IssuedWhom')  # Field name made lowercase. This field type is a guess.
    director = models.TextField(db_column='Director', blank=True,
                                null=True)  # Field name made lowercase. This field type is a guess.
    iduser = models.ForeignKey('User', models.DO_NOTHING, db_column='IDUser')  # Field name made lowercase.

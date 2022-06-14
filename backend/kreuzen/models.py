from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Subject(models.Model):
    """
    A class representing a subject, e.g. 'Pharmakologie' or 'Chirurgie'

    ...

    Attributes
    ----------
    fach_name : str
        the name of the subject (max_length=50)
    """

    fach_name = models.CharField(max_length=50)

    # TODO: do i need this class or could it just be a CharField inside Exam?

    def __str__(self) -> str:
        return self.fach_name


class Exam(models.Model):
    """
    A class representing an exam

    ...

    Attributes
    ----------
    semester : str
        The semester the exam was written in TODO english
    subject : ForeignKey
        The subject of the exam
    date_of_exam : date
        The date the exam was writte on
    details : str
        Specifying the details of the exam, e.g. Rigo or second exam
    """

    semester = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_of_exam = models.DateTimeField('date created')

    def __str__(self) -> str:
        return f"{self.fach.fach_name}-{self.semester}"


class Tag(models.Model):
    """
    A class representing a tag

    Tags are providing the categorization of questions

    ...

    Attributes
    ----------
    tag_text : str
        Naming the tag
    subject : str
        Tags are specific for subjects
    """

    tag_text = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.tag_text


class Answer(models.Model):
    """
    A class representing an answer of a question

    ...

    Attributes
    ----------
    text : str
        Answer text
    is_right : boolean
        True if the answer is true
    frequency : float
        The frequency of what users chose this answer #TODO: make only the first choice count
    """

    text = models.CharField()
    is_right = models.BooleanField(default=False)
    frequency = models.FloatField()


class Question(models.Model):
    """
    A class representing a question

    ...

    Attributes
    ----------
    text : str
        Question text
    date_created : date (DateTimeField)
        The date the question was created
    created_by : ForeignKey -> User
        The user that created the question
    exam : Foreign Key -> Exam
        The exam the question belongs to #TODO: make question with exam field or exam with questions field??
    tags : ManyToManyField -> Tag
        The tags of the question
    answers : ManyToManyField -> Answer
        The answers of the question
    img : ImageField
        The image corresponding to the question if it exists
    is_reported : boolean
        True if the question is reported
    reported_text : str
        Text which about the error in the question
    """

    text = models.CharField(max_length=1000)
    date_created = models.DateTimeField('date created', default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, on_delete=models.CASCADE)

    answers = models.ManyToManyField(Answer, on_delete=models.CASCADE)

    # TODO: are we just saving the link or the actual image
    img = models.ImageField(blank=True)

    # Question can be reported -> and also the reason why
    is_reported = models.BooleanField(default=False)
    # TODO: maybe separate it from question to bug app?
    reported_text = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.question_text


class Session(models.Model):
    """
    A class representing a Session.

    ...

    Attributes
    ----------
    name : str
        The name of the session
    questions : ManyToManyField -> Question
        The questions that are in the session
    date_created : date
        The date the session was created on
    user : ForeignKey -> User
        The user that the sessions belongs to
    is_finished : boolean
        True if all questions are answered #TODO: do i need this value or can i just compute it
    num_questions : int
        The number of questions in the session
    num_solved_questions : int
        The number of SOLVED questions in the session
    num_correctly_solved_questions : int
        The number of CORRECTLY solved questions in the session
    solved_questions : list #TODO Is it a list?
        List of all solved_questions
    correctly_solved_questions : list #TODO Is it a list?
        List of all CORRECTLY solved questions
    """

    name = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, through="ActiveSession")
    date_created = models.DateTimeField('date created', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    # def calculateSolvedQuestions(self):
    #     return self.questions.filter(activesession__is_solved=True).count()

    # def calculateCorrectlySolvedQuestions(self):
    #     return self.questions.filter(activesession__is_correctly_solved=True).count()

    def returnSolvedQuestions(self):
        return self.questions.filter(activesession__is_solved=True)

    def returnCorrectlySolvedQuestions(self):
        return self.questions.filter(activesession__is_correctly_solved=True)

    def calculateNumberOfQuestions(self):
        return self.questions.all().count()

    num_questions = property(calculateNumberOfQuestions)
    # num_solved_questions = property(calculateSolvedQuestions)
    # num_correctly_solved_questions = property(
    #     calculateCorrectlySolvedQuestions)

    solved_questions = property(returnSolvedQuestions)
    correctly_solved_questions = property(returnCorrectlySolvedQuestions)

    # Auswertung?

    def __str__(self) -> str:
        return self.session_name


class ActiveSession(models.Model):
    # TODO: better name
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    is_viewed = models.BooleanField(default=False)
    is_solved = models.BooleanField(default=False)
    is_correctly_solved = models.BooleanField(default=False)
    is_marked = models.BooleanField(default=False)  # TODO: is this necessary?


class Collection(models.Model):
    collection_name = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created', default=timezone.now)
    questions = models.ManyToManyField(Question)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.collection_name

from django.db import models

class  Project(models.Model): #fails to pluralize?
    name = models.CharField(max_length=100)
    is_mini = models.BooleanField(default=False)
    motivation = models.TextField(blank=True)
    elaboration = models.TextField(blank=True)
    date = models.DateField(null=True)
    used_skills = models.ManyToManyField('skills.Skill', blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    # all foreign below: images, videos, codes, documents, links, rest_files

    def __str__(self):
        return self.name

class Category(models.Model): # will be used for search
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='projects/media/images/')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

class Video(models.Model):
    name = models.CharField(max_length=100, blank=True)
    embeded = models.TextField() # use youtube link

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Code(models.Model):
    code = models.TextField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

class Document(models.Model): #pdf, doc, etc goes
    document = models.FileField(upload_to='projects/media/documents/')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

class Link(models.Model):
    name = models.CharField(max_length=100, blank=True)
    link = models.TextField()

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class Rest_File(models.Model): # all other files beside document
    rest_file = models.FileField(upload_to='projects/media/rest_files/')

    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
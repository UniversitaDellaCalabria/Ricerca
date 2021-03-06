"""
Django settings for ricerca project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from .settingslocal import *

MIDDLEWARE = [
    # 'silk.middleware.SilkyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    # SameSite Cookie workaround
    #  'djangosaml2.middleware.SamlSessionMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True

# GETTEXT LOCALIZATION
MIDDLEWARE.append('django.middleware.locale.LocaleMiddleware')
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)
#

ROOT_URLCONF = 'ricerca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ricerca.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# from django 3.2
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# MAPPING LABEL

LABEL_MAPPING = {
    'en': {
        'RegDidId': 'Teaching Regulation ID',
        'RegDidState': 'Teaching Regulation State',
        'CdSId': 'Course of Study ID',
        'AcademicYear': 'Academic Year',
        'CdSName': 'Course of Study Name',
        'DepartmentId': 'Department ID',
        'DepartmentName': 'Department',
        'DepartmentNameShort': 'Department Name Short',
        'CourseType': 'Course Type',
        'CourseTypeDescription': 'Course Type',
        'CourseClassId': 'Course Class ID',
        'CourseClassName': 'Course Class Name',
        'CdSLanguage': 'Language',
        'CdSDuration': 'Duration',
        'CdSECTS': 'ECTS',
        'CdSAttendance': 'Attendance',
        'CdSIntro': 'Intro',
        'CdSDoc': 'Document',
        'CdSVideo': 'Video',
        'CdSGoals': 'Goals',
        'CdSAccess': 'Access',
        'CdSAdmission': 'Admission',
        'CdSProfiles': 'Profiles',
        'CdSFinalTest': 'Final Test',
        'CdSFinalTestMode': 'Final Test Mode',
        'CdSSatisfactionSurvey': 'Satisfaction Survey',
        'StudyPlanId': 'Study Plan ID',
        'StudyPlanName': 'Study Plan Name',
        'StudyPlanCod': 'Study Plan Code',
        'StudyActivities': 'Study Activities',
        'StudyActivityRegDidId': 'Teaching Regulation ID',
        'StudyActivityID': 'Study Activity ID',
        'StudyActivityName': 'Study Activity',
        'StudyActivityCdSID': 'Course of Study ID',
        'StudyActivityYear': 'Year',
        'StudyActivitySemester': 'Semester',
        'StudyActivityECTS': 'ECTS',
        'StudyActivitySSD': 'SSD',
        'StudyActivityCompulsory': 'Compulsory',
        'StudyActivityCdSName': 'Course of Study',
        'StudyActivityTeachingUnitType': 'Teaching Unit Type',
        'StudyActivityTeacherID': 'Teacher ID',
        'StudyActivityTeacherName': 'Teacher',
        'StudyActivityContent': 'Content',
        'StudyActivityProgram': 'Program',
        'StudyActivityLearningOutcomes': 'Learning Outcomes',
        'StudyActivityMethodology': 'Methodology',
        'StudyActivityEvaluation': 'Evaluation',
        'StudyActivityTextbooks': 'Textbooks',
        'StudyActivityWorkload': 'Workload',
        'StudyActivityElearningLink': 'E-Learning Link',
        'StudyActivityElearningInfo': 'E-Learning Info',
        'StudyActivityPrerequisites': 'Prerequisites',
        'StudyActivitiesModules': 'Modules',
        'StudyActivityAA': 'Academic Year',
        'StudyActivityLanguage': 'Language',
        'StudyActivityRoot': 'Study Activity Root',
        'StudyActivityBorrowedFrom': 'Borrowed from',
        'StudyActivitiesBorrowedFromThis': 'Borrowed from this',
        'TeacherID': 'Teacher ID',
        'TeacherName': 'Name',
        'TeacherRole': 'Role',
        'TeacherRoleDescription': 'Role',
        'TeacherSSD': 'SSD',
        'TeacherDepartmentID': 'Department ID',
        'TeacherDepartmentName': 'Department',
        'TeacherSSDCod': 'SSD',
        'TeacherSSDDescription': 'SSD',
        'TeacherCode': 'Teacher Code',
        'TeacherFirstName': 'First Name',
        'TeacherLastName': 'Last Name',
        'TeacherOffice': 'Office',
        'TeacherOfficeReference': 'Office Reference',
        'TeacherEmail': 'Email',
        'TeacherPEC': 'PEC',
        'TeacherPrivateEmail': 'Private Email',
        'TeacherTelOffice': 'Office Phone',
        'TeacherTelCelOffice': 'Office Mobile Phone',
        'TeacherTelCel': 'Mobile Phone',
        'TeacherTelDomicile': 'Domicile Phone',
        'TeacherTelResidence': 'Residence Phone',
        'TeacherFax': 'Fax',
        'TeacherSkype': 'Skype',
        'TeacherWebSite': 'URL Web Site',
        'TeacherCV': 'Curriculum Vitae',
        'Office': 'Office',
        'OfficeReference': 'Office Reference',
        'Email': 'Email',
        'PEC': 'PEC',
        'PrivateEmail': 'Private Email',
        'TelOffice': 'Office Phone',
        'TelCelOffice': 'Office Mobile Phone',
        'TelCel': 'Mobile Phone',
        'TelDomicile': 'Domicile Phone',
        'TelResidence': 'Residence Phone',
        'Fax': 'Fax',
        'Skype': 'Skype',
        'WebSite': 'URL Web Site',
        'CV': 'Curriculum Vitae',
        'Contacts': 'Contacts',
        'Function': 'Function',
        'Structure': 'Structure',
        'Role': 'Role',
        'RoleDescription': 'Role',
        'ID': 'ID',
        'Name': 'Name',
        'RGroupID': 'Group ID',
        'RGroupName': 'Group Name',
        'RGroupDescription': 'Group Description',
        'R&SLineID': 'Research Line ID',
        'R&SLineDescription': 'Description',
        'R&SLineResults': 'Results',
        'R&SLineERC0Id': 'ERC0 ID',
        'R&SLineERC0Name': 'ERC0 Name',
        'DepartmentID': 'Department ID',
        'DoctorateCdsCOD': 'Course of Study Code',
        'DoctorateCdsName': 'Course of Study Name',
        'DoctorateRegID': 'Doctorate Regulation ID',
        'DoctorateRegCOD': 'Doctorate Regulation Code',
        'DoctorateCdSDuration': 'Duration',
        'DoctorateCdSECTS': 'ECTS',
        'DoctorateCdSAttendance': 'Attendance',
        'CourseName': 'Course Name',
        'CycleNumber': 'Cycle Number',
        'StudyPlanCOD': 'Study Plan Code',
        'StudyPlanDes': 'Study Plan Description',
        'FUNZIONI': 'Tasks',
        'COMPETENZE': 'Skills',
        'SBOCCHI': 'Job Opportunities',
        'StructureId': 'Structure Id',
        'StructureTypeName': 'Structure Type Name',
        'StructureName': 'Structure Name',
        'StructureTypeCOD': 'Structure Type COD',
    },
    'it': {
        'RegDidId': 'ID Regolamento Didattico',
        'RegDidState': 'Stato del Regolamento Didattico',
        'CdSId': 'ID Corso di Studi',
        'AcademicYear': 'Anno Accademico',
        'CdSName': 'Nome Corso di Studi',
        'DepartmentId': 'ID Dipartimento',
        'DepartmentName': 'Nome Dipartimento',
        'DepartmentNameShort': 'Nome Dipartimento Breve',
        'CourseType': 'Tipologia Corso',
        'CourseTypeDescription': 'Tipologia Corso',
        'CourseClassId': 'ID Classe Corso',
        'CourseClassName': 'Classe Corso',
        'CdSLanguage': 'Lingua',
        'CdSDuration': 'Durata',
        'CdSECTS': 'ECTS',
        'CdSAttendance': 'Frequenza Obbligatoria',
        'CdSIntro': 'Descrizione',
        'CdSDoc': 'Documento',
        'CdSVideo': 'Video',
        'CdSGoals': 'Obiettivi',
        'CdSAccess': 'Accesso',
        'CdSAdmission': 'Ammissione',
        'CdSProfiles': 'Profili',
        'CdSFinalTest': 'Test Finale',
        'CdSFinalTestMode': 'Modalità Test Finale',
        'CdSSatisfactionSurvey': 'Soddisfazione e condizione occupazionale (fonte Almalaurea)',
        'StudyPlanId': 'ID Piano di Studi',
        'StudyPlanName': 'Piano di Studi',
        'StudyPlanCod': 'Codice Piano di Studi',
        'StudyActivities': 'Attività Formative',
        'StudyActivityID': 'ID Attività Formativa',
        'StudyActivityRegDidId': 'ID Regolamento Didattico',
        'StudyActivityName': 'Nome Attività Formativa',
        'StudyActivityCdSID': 'Codice Corso di Studi',
        'StudyActivityYear': 'Anno Corso',
        'StudyActivitySemester': 'Semestre',
        'StudyActivityECTS': 'ECTS',
        'StudyActivitySSD': 'SSD',
        'StudyActivityCompulsory': 'Frequenza Obbligatoria',
        'StudyActivityCdSName': 'Corso di Studi',
        'StudyActivityTeachingUnitType': 'Tipologia Insegnamento',
        'StudyActivityTeacherID': 'Matricola Docente',
        'StudyActivityTeacherName': 'Docente',
        'StudyActivityContent': 'Contenuti',
        'StudyActivityProgram': 'Programma',
        'StudyActivityLearningOutcomes': 'Obiettivi Formativi',
        'StudyActivityMethodology': 'Metodologie Didattiche',
        'StudyActivityEvaluation': 'Metodi di Valutazione',
        'StudyActivityTextbooks': 'Testi di Riferimento',
        'StudyActivityWorkload': 'Carico di Lavoro',
        'StudyActivityElearningLink': 'Link Aula Virtuale',
        'StudyActivityElearningInfo': 'Info per l\'Accesso all\'Aula Virtuale',
        'StudyActivityPrerequisites': 'Prerequisiti',
        'StudyActivitiesModules': 'Moduli',
        'StudyActivityAA': 'Anno Accademico',
        'StudyActivityLanguage': 'Lingua',
        'StudyActivityRoot': 'Attività Formativa Principale',
        'StudyActivityBorrowedFrom': 'Mutuata da',
        'StudyActivitiesBorrowedFromThis': 'Mutuate da questa',
        'TeacherID': 'ID Docente',
        'TeacherName': 'Nome',
        'TeacherRole': 'Ruolo',
        'TeacherRoleDescription': 'Ruolo',
        'TeacherSSD': 'SSD',
        'TeacherDepartmentID': 'ID Dipartimento',
        'TeacherDepartmentName': 'Dipartimento',
        'TeacherSSDCod': 'SSD',
        'TeacherSSDDescription': 'SSD',
        'TeacherCode': 'Codice Fiscale',
        'TeacherFirstName': 'Nome',
        'TeacherLastName': 'Cognome',
        'TeacherOffice': 'Ufficio',
        'TeacherOfficeReference': 'Riferimento Ufficio',
        'TeacherEmail': 'Posta Elettronica',
        'TeacherPEC': 'Posta Elettronica Certificata',
        'TeacherPrivateEmail': 'Posta Elettronica Privata',
        'TeacherTelOffice': 'Telefono Ufficio',
        'TeacherTelCelOffice': 'Telefono Cellulare Ufficio',
        'TeacherTelCel': 'Telefono Cellulare',
        'TeacherTelDomicile': 'Telefono Domicilio',
        'TeacherTelResidence': 'Telefono Residenza',
        'TeacherFax': 'Fax',
        'TeacherSkype': 'Skype',
        'TeacherWebSite': 'URL Sito WEB',
        'TeacherCV': 'Curriculum Vitae',
        'Office': 'Ufficio',
        'OfficeReference': 'Riferimento Ufficio',
        'Email': 'Posta Elettronica',
        'PEC': 'Posta Elettronica Certificata',
        'PrivateEmail': 'Posta Elettronica Privata',
        'TelOffice': 'Telefono Ufficio',
        'TelCelOffice': 'Telefono Cellulare Ufficio',
        'TelCel': 'Telefono Cellulare',
        'TelDomicile': 'Telefono Domicilio',
        'TelResidence': 'Telefono Residenza',
        'Fax': 'Fax',
        'Skype': 'Skype',
        'WebSite': 'URL Sito WEB',
        'CV': 'Curriculum Vitae',
        'Contacts': 'Contatti',
        'Function': 'Funzione',
        'Structure': 'Struttura',
        'Role': 'Ruolo',
        'RoleDescription': 'Ruolo',
        'ID': 'ID',
        'Name': 'Nome',
        'RGroupID': 'ID Gruppo di Ricerca',
        'RGroupName': 'Nome Gruppo di Ricerca',
        'RGroupDescription': 'Descrizione Gruppo di Ricerca',
        'R&SLineID': 'ID Linea di Ricerca',
        'R&SLineDescription': 'Descrizione Linea di Ricerca',
        'R&SLineResults': 'Risultati Linea di Ricerca',
        'R&SLineERC0Id': 'ID Linea di Ricerca ERC0',
        'R&SLineERC0Name': 'Nome Linea di Ricerca ERC0',
        'DepartmentID': 'ID Dipartimento',
        'DoctorateCdsCOD': 'Codice Corso di Studi',
        'DoctorateCdsName': 'Nome Corso di Studi',
        'DoctorateRegID': 'ID Regolamento Dottorato',
        'DoctorateRegCOD': 'Codice Regolamento Dottorato',
        'DoctorateCdSDuration': 'Durata',
        'DoctorateCdSECTS': 'ECTS',
        'DoctorateCdSAttendance': 'Frequenza Obbligatoria',
        'CourseName': 'Nome Corso',
        'CycleNumber': 'Numero Ciclo',
        'StudyPlanCOD': 'Codice Piano di Studi',
        'StudyPlanDes': 'Descrizione Piano di Studi',
        'FUNZIONI': 'Funzioni',
        'COMPETENZE': 'Competenze',
        'SBOCCHI': 'Sbocchi',
        'StructureId': 'Id Struttura',
        'StructureTypeName': 'Nome Tipologia Struttura',
        'StructureName': 'Nome Struttura',
        'StructureTypeCOD': 'Codice Struttura',
    }
}

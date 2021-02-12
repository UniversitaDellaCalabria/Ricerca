

from django.http import QueryDict
from rest_framework import generics, permissions


from .filters import *
from .serializers import *
from .services import *
from .pagination import UnicalStorageApiPagination


# permissions.IsAuthenticatedOrReadOnly
# allow authenticated users to perform any request. Requests for
# unauthorised users will only be permitted if the request method is
# one of the "safe" methods; GET, HEAD or OPTIONS

class ApiResourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    allowed_methods = ('GET',)

    def perform_create(self, serializer):
        serializer.save(user_ins=self.request.user)


class ApiResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    allowed_methods = ('GET',)

    def perform_update(self, serializer):
        serializer.save(user_mod=self.request.user)


# =================================================


class ApiPersonaleList(ApiResourceList):
    description = 'Available Personale, Professors and Researchers'
    queryset = Personale.objects.all()
    serializer_class = PersonaleSerializer


class ApiPersonaleDetail(ApiResourceDetail):
    description = 'Detail of Persona'
    queryset = Personale.objects.all()
    serializer_class = PersonaleSerializer


# =================================================

class ApiRicercaAster1List(ApiResourceList):
    description = 'Available Aster 1'
    queryset = RicercaAster1.objects.all()
    serializer_class = RicercaAster1Serializer


class ApiRicercaAster1Detail(ApiResourceDetail):
    description = 'Aster 1 Details'
    queryset = RicercaAster1.objects.all()
    serializer_class = RicercaAster1Serializer


# =================================================

class ApiRicercaAster2List(ApiResourceList):
    description = 'Available Aster 2'
    queryset = RicercaAster2.objects.all()
    serializer_class = RicercaAster2Serializer


class ApiRicercaAster2Detail(ApiResourceDetail):
    description = 'Aster 2 Details'
    queryset = RicercaAster2.objects.all()
    serializer_class = RicercaAster2Serializer


# =================================================

class ApiRicercaErc1List(ApiResourceList):
    description = 'Available Erc 1'
    queryset = RicercaErc1.objects.all()
    serializer_class = RicercaErc1Serializer


class ApiRicercaErc1Detail(ApiResourceDetail):
    description = 'Erc 1 Details'
    queryset = RicercaErc1.objects.all()
    serializer_class = RicercaErc1Serializer


# =================================================

class ApiRicercaErc2List(ApiResourceList):
    description = 'Available Erc 2'
    queryset = RicercaErc2.objects.all()
    serializer_class = RicercaErc2Serializer


class ApiRicercaErc2Detail(ApiResourceDetail):
    description = 'Erc 2 Details'
    queryset = RicercaErc2.objects.all()
    serializer_class = RicercaErc2Serializer


# =================================================

class ApiRicercaDocenteGruppoList(ApiResourceList):
    description = 'List of Professors/Researchers in which Research Groups'
    queryset = RicercaDocenteGruppo.objects.all()
    serializer_class = RicercaDocenteGruppoSerializer


class ApiRicercaDocenteGruppoDetail(ApiResourceDetail):
    description = 'Details of Professors/Researchers in which Research Groups'
    queryset = RicercaDocenteGruppo.objects.all()
    serializer_class = RicercaDocenteGruppoSerializer


# =================================================

class ApiRicercaDocenteLineaApplicataList(ApiResourceList):
    description = 'List of Professors/Researchers and Applied Lines'
    queryset = RicercaDocenteLineaApplicata.objects.all()
    serializer_class = RicercaDocenteLineaApplicataSerializer


class ApiRicercaDocenteLineaApplicataDetail(ApiResourceDetail):
    description = 'Details of a Professor/Researcher in an Applied Line'
    queryset = RicercaDocenteLineaApplicata.objects.all()
    serializer_class = RicercaDocenteLineaApplicataSerializer


# =================================================

class ApiRicercaDocenteLineaBaseList(ApiResourceList):
    description = 'List of Base Lines'
    queryset = RicercaDocenteLineaBase.objects.all()
    serializer_class = RicercaDocenteLineaBaseSerializer


class ApiRicercaDocenteLineaBaseDetail(ApiResourceDetail):
    description = 'Details about a Base Line'
    queryset = RicercaDocenteLineaBase.objects.all()
    serializer_class = RicercaDocenteLineaBaseSerializer


# =================================================

class ApiRicercaGruppoList(ApiResourceList):
    description = 'List of Research Groups'
    queryset = RicercaGruppo.objects.all()
    serializer_class = RicercaGruppoSerializer


class ApiRicercaGruppoDetail(ApiResourceDetail):
    description = 'Details of a Research Group'
    queryset = RicercaGruppo.objects.all()
    serializer_class = RicercaGruppoSerializer


# =================================================

class ApiRicercaLineaApplicataList(ApiResourceList):
    description = 'List of Applied Lines'
    queryset = RicercaLineaApplicata.objects.all()
    serializer_class = RicercaLineaApplicataSerializer


class ApiRicercaLineaApplicataDetail(ApiResourceDetail):
    description = 'Detail of an Applied Line'
    queryset = RicercaLineaApplicata.objects.all()
    serializer_class = RicercaLineaApplicataSerializer


# =================================================

class ApiRicercaLineaBaseList(ApiResourceList):
    description = 'List of Base Lines'
    queryset = RicercaLineaBase.objects.all()
    serializer_class = RicercaLineaBaseSerializer


class ApiRicercaLineaBaseDetail(ApiResourceDetail):
    description = 'Details of a Base Line'
    queryset = RicercaLineaBase.objects.all()
    serializer_class = RicercaLineaBaseSerializer


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


class ApiEndpoint(generics.GenericAPIView):
    pagination_class = UnicalStorageApiPagination

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.language = None

    def get(self, obj):
        self.language = str(
            self.request.query_params.get(
                'language', 'it')).lower()
        queryset = self.get_queryset()

        # TODO: pagination custom
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        results = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(results)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'language': self.language})
        return context


class ApiCdSList(ApiEndpoint):
    description = ''
    serializer_class = CdSListSerializer
    filter_backends = [ApiCdsListFilter]

    def get_queryset(self):
        return ServiceDidatticaCds.cdslist(
            self.language, self.request.query_params)


class ApiCdSInfo(ApiEndpoint):
    description = ''
    serializer_class = CdsInfoSerializer
    filter_backends = [ApiCdsInfoFilter]

    # [?] Required Parameters (e.g. cdsid in this case), handle via urls?
    def get_queryset(self):
        cdsid_param = self.request.query_params.get('cdsid')
        if not cdsid_param:
            return None

        res = ServiceDidatticaCds.cdslist(
            self.language, QueryDict(
                'regdid_id=' + cdsid_param))
        res = list(res)

        if(len(res) == 0):
            return None

        texts = DidatticaTestiRegolamento.objects.filter(regdid=cdsid_param)\
            .values('regdid__regdid_id', 'clob_txt_ita', 'clob_txt_eng', 'tipo_testo_regdid_cod', 'profilo', 'profilo_eng')

        list_profiles = {}
        last_profile = ""

        res[0]['DESC_COR_BRE'] = None
        res[0]['OBB_SPEC'] = None
        res[0]['REQ_ACC'] = None
        res[0]['REQ_ACC_2'] = None
        res[0]['PROFILO'] = None
        res[0]['PROVA_FINALE'] = None
        res[0]['PROVA_FINALE_2'] = None

        for text in texts:
            if text['tipo_testo_regdid_cod'] != 'FUNZIONI' and text['tipo_testo_regdid_cod'] != 'COMPETENZE' and text['tipo_testo_regdid_cod'] != 'SBOCCHI':
                res[0][text['tipo_testo_regdid_cod']] = text[
                    f'clob_txt_{self.language == "it" and "ita" or "eng"}']
            else:
                if text[f'{ self.language == "it" and "profilo" or "profilo_eng" }'] != last_profile:
                    last_profile = text[f'{self.language == "it" and "profilo" or "profilo_eng"}']
                    list_profiles[last_profile] = {}
                list_profiles[last_profile][text['tipo_testo_regdid_cod']
                                            ] = text[f'clob_txt_{self.language == "it" and "ita" or "eng"}']

        res[0]['PROFILO'] = list_profiles
        return res


class ApiCdSStudyPlans(ApiEndpoint):
    description = ''
    serializer_class = CdSStudyPlansSerializer
    filter_backends = [ApiCdSStudyPlansFilter]

    def get_queryset(self):
        cdsid_param = self.request.query_params.get('cdsid')
        if not cdsid_param:
            return None

        # problemi con year = null, provare regdidid = 6343
        # Fare test
        # Chiedere corsi principali/moduli sottomoduli

        return ServiceDidatticaAttivitaFormativa.getListAttivitaFormativa(
            regdid_id=cdsid_param)


class ApiStudyPlansActivities(ApiEndpoint):
    description = ''
    serializer_class = StudyPlansActivitiesSerializer
    #filter_backends = [ApiCdsListFilter]

    def get_queryset(self):
        studyplanid_param = self.request.query_params.get('studyplanid')
        if not studyplanid_param:
            return None

        return ServiceDidatticaAttivitaFormativa.getAttivitaFormativaByStudyPlan(
            studyplanid=studyplanid_param)


class ApiStudyActivityInfo(ApiEndpoint):
    description = ''
    serializer_class = StudyActivityInfoSerializer

    # filter_backends = [ApiCdsListFilter]

    def get_queryset(self):
        studyactivityid = self.request.query_params.get('studyactivityid')
        if not studyactivityid:
            return None

        return ServiceDidatticaAttivitaFormativa.getAttivitaFormativaWithSubModules(
            af_id=studyactivityid, language=self.language)


class ApiCdSMainTeachers(ApiEndpoint):
    description = ''
    serializer_class = CdSMainTeachersSerializer
    # filter_backends = [ApiCdsListFilter]

    def get_queryset(self):
        regdid_id = self.request.query_params.get('cdsid')
        if not regdid_id:
            return None

        return ServiceDidatticaAttivitaFormativa.getDocentiPerReg(regdid_id)

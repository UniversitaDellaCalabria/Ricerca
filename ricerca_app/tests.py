from django.test import TestCase, Client
from django.urls import reverse

from .util_test import ComuniAllUnitTest, DidatticaAttivitaFormativaUnitTest, DidatticaCdsLinguaUnitTest, DidatticaCdsUnitTest, DidatticaCoperturaUnitTest, DidatticaDipartimentoUnitTest, DidatticaPdsRegolamentoUnitTest, DidatticaRegolamentoUnitTest, DidatticaTestiAfUnitTest, DidatticaTestiRegolamentoUnitTest, PersonaleUnitTest, RicercaAster1UnitTest, RicercaAster2UnitTest, RicercaDocenteGruppoUnitTest, RicercaDocenteLineaApplicataUnitTest, RicercaDocenteLineaBaseUnitTest, RicercaErc1UnitTest, RicercaErc2UnitTest, RicercaGruppoUnitTest, RicercaLineaApplicataUnitTest, RicercaLineaBaseUnitTest, TerritorioItUnitTest
from .serializers import CreateUpdateAbstract


class ApiCdSListUnitTest(TestCase):

    def test_apicdslist(self):
        req = Client()
        # user = ContextUnitTest.create_user(username='staff',is_staff=True)

        dip = DidatticaDipartimentoUnitTest.create_didatticaDipartimento(**{
            'dip_id': 1,
        })
        didatticaCds = DidatticaCdsUnitTest.create_didatticaCds(**{
            'dip': dip,
        })
        DidatticaCdsLinguaUnitTest.create_didatticaCdsLingua(**{
            'cdsord': didatticaCds,
        })
        DidatticaRegolamentoUnitTest.create_didatticaRegolamento(**{
            'regdid_id': 1,
            'stato_regdid_cod': 'A',
            'titolo_congiunto_cod': 'N',
            'cds_id': 1,
        })

        url = reverse('ricerca:cdslist')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        # param: language
        data = {'language': 'it'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: language
        data = {'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: coursetype
        data = {'coursetype': '1'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: courseclassid
        data = {'courseclassid': '1'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: courseclassname
        data = {'courseclassname': 'laurea in informatica'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: courseclassgroup
        # data = {'courseclassgroup': ''}
        # res = req.get(url, data=data)
        # assert res.json()[0]['RegDidId'] == 1

        # param: departmentid
        data = {'departmentid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: departmentname
        data = {'departmentname': 'matematica e informatica'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: academicyear
        data = {'academicyear': 2020}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: jointdegree
        data = {'jointdegree': 'N'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: cdslanguage
        data = {'cdslanguage': 'ITALIANO'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: keywords ita
        data = {'keywords': 'informatica'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: keywords eng
        data = {'keywords': 'computer', 'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: keywords eng wrong
        data = {'keywords': 'math', 'language': 'eng'}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 0

        # param: all
        data = {'cdslanguage': 'ITALIAN',
                'jointdegree': 'N',
                'academicyear': 2020,
                'departmentname': 'math and computer science',
                'departmentid': 1,
                'courseclassname': 'laurea in informatica',
                'courseclassid': '1',
                'coursetype': '1',
                'language': 'eng',
                }
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1


class OpenApiSchemaUnitTest(TestCase):
    def test_openapi(self):
        req = Client()
        url = reverse('ricerca:openapi-schema')
        res = req.get(url)
        assert res.status_code == 200


class SerializersUnitTest(TestCase):
    def test_createUpdateAbstract(self):
        ser = CreateUpdateAbstract()
        ser.create(None)
        ser.update(None, None)


class ModelsToStringUnitTest(TestCase):

    def test_modelstostring(self):
        comuni_all = ComuniAllUnitTest.create_comuniAll(**{
            'id_comune': 1
        })
        assert isinstance(comuni_all.__str__(), str)

        territorio_it = TerritorioItUnitTest.create_territorioIt(**{
            'cd_catasto': comuni_all
        })
        assert isinstance(territorio_it.__str__(), str)

        dip = DidatticaDipartimentoUnitTest.create_didatticaDipartimento(**{
            'dip_id': 1,
        })
        assert isinstance(dip.__str__(), str)

        didattica_cds = DidatticaCdsUnitTest.create_didatticaCds(**{
            'dip': dip,
        })
        assert isinstance(didattica_cds.__str__(), str)

        didattica_lingua = DidatticaCdsLinguaUnitTest.create_didatticaCdsLingua(
            **{'cdsord': didattica_cds, })
        assert isinstance(didattica_lingua.__str__(), str)

        didattica_regolamento = DidatticaRegolamentoUnitTest.create_didatticaRegolamento(
            **{'regdid_id': 1, })
        assert isinstance(didattica_regolamento.__str__(), str)

        didattica_testi_regolamento = DidatticaTestiRegolamentoUnitTest.create_didatticaTestiRegolamento(
            **{'regdid': didattica_regolamento, })
        assert isinstance(didattica_testi_regolamento.__str__(), str)


class ApiCdSInfoUnitTest(TestCase):

    def test_apicdslist(self):
        req = Client()

        dip = DidatticaDipartimentoUnitTest.create_didatticaDipartimento(**{
            'dip_id': 1,
        })
        didatticaCds = DidatticaCdsUnitTest.create_didatticaCds(**{
            'dip': dip,
        })
        DidatticaCdsLinguaUnitTest.create_didatticaCdsLingua(**{
            'cdsord': didatticaCds,
        })
        reg = DidatticaRegolamentoUnitTest.create_didatticaRegolamento(**{
            'regdid_id': 1,
            'stato_regdid_cod': 'A',
            'titolo_congiunto_cod': 'N',
            'cds': didatticaCds,
        })
        DidatticaTestiRegolamentoUnitTest.create_didatticaTestiRegolamento(**{
            'txt_id': 1,
            'regdid': reg,
            'tipo_testo_regdid_cod': 'DESC_COR_BRE',
        })
        DidatticaTestiRegolamentoUnitTest.create_didatticaTestiRegolamento(**{
            'txt_id': 2,
            'regdid': reg,
            'tipo_testo_regdid_cod': 'FUNZIONI',
            'profilo': 'profiloprova',
            'clob_txt_ita': 'provadescrizione',
        })

        url = reverse('ricerca:cdsinfo')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        # param: language
        data = {'language': 'it', 'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: cdsid 10 doesn't exist
        data = {'language': 'it', 'cdsid': 10}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 0

        # param: language
        data = {'language': 'eng', 'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # param: language
        data = {'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][
            0]['CdSProfiles']['profiloprova']['FUNZIONI'] == 'provadescrizione'


class ApiCdSStudyPlansUnitTest(TestCase):

    def test_apicdslist(self):
        req = Client()

        regdid = DidatticaRegolamentoUnitTest.create_didatticaRegolamento()
        pds = DidatticaPdsRegolamentoUnitTest.create_didatticaPdsRegolamento(
            **{'regdid': regdid, })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'pds_regdid': pds,
            'regdid': regdid,
            'des': 'matematica',
            'af_gen_des_eng': 'math',
            'af_id': 1,
            'af_radice_id': 1,
        })

        url = reverse('ricerca:cdsstudyplans')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RegDidId'] == 1

        # language it
        data = {'cdsid': 1, 'language': 'it'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityName'] == 'matematica'

        # language eng
        data = {'cdsid': 1, 'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityName'] == 'math'


class ApiStudyPlansActivitiesUnitTest(TestCase):

    def test_apistudyplansactivities(self):
        req = Client()

        regdid = DidatticaRegolamentoUnitTest.create_didatticaRegolamento()
        pds1 = DidatticaPdsRegolamentoUnitTest.create_didatticaPdsRegolamento(
            **{'pds_regdid_id': 1, 'regdid': regdid, })
        pds2 = DidatticaPdsRegolamentoUnitTest.create_didatticaPdsRegolamento(
            **{'pds_regdid_id': 2, 'regdid': regdid, })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 1,
            'pds_regdid': pds1,
            'des': 'matematica',
            'af_gen_des_eng': 'math',
            'ciclo_des': 'Primo semestre',
            'regdid': regdid,
            'af_radice_id': 1,
        })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 2,
            'pds_regdid': pds1,
            'des': 'informatica',
            'af_gen_des_eng': 'computer science',
            'ciclo_des': 'Secondo semestre',
            'regdid': regdid,
            'af_radice_id': 2,
        })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 3,
            'pds_regdid': pds1,
            'des': 'informatica modulo 1',
            'af_gen_des_eng': 'computer science modulo 1',
            'ciclo_des': 'Secondo semestre',
            'regdid': regdid,
            'af_radice_id': 2,
        })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 4,
            'pds_regdid': pds2,
            'des': 'matematica2',
            'af_gen_des_eng': 'math2',
            'ciclo_des': 'Primo semestre',
            'regdid': regdid,
            'af_radice_id': 4,
        })

        url = reverse('ricerca:studyplansactivities')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'studyplanid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityID'] == 1

        # 3 courses : 2 main courses, 1 module course, should return 2 courses
        data = {'studyplanid': 1}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 2

        # language it first semester
        data = {'studyplanid': 1, 'language': 'it'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityName'] == 'matematica'

        # language eng first semester
        data = {'studyplanid': 1, 'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityName'] == 'math'

        # language it second semester
        data = {'studyplanid': 1, 'language': 'it'}
        res = req.get(url, data=data)
        assert res.json()['results'][1]['StudyActivityName'] == 'informatica'

        # language eng second semester
        data = {'studyplanid': 1, 'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()[
            'results'][1]['StudyActivityName'] == 'computer science'

        data = {'studyplanid': 2}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityID'] == 4


class ApiStudyActivityInfoUnitTest(TestCase):

    def test_apistudyactivityinfo(self):
        req = Client()

        regdid = DidatticaRegolamentoUnitTest.create_didatticaRegolamento()
        pds = DidatticaPdsRegolamentoUnitTest.create_didatticaPdsRegolamento(
            **{'pds_regdid_id': 1, 'regdid': regdid, })
        course = DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 1,
            'pds_regdid': pds,
            'des': 'informatica',
            'af_gen_des_eng': 'computer science',
            'ciclo_des': 'Primo semestre',
            'regdid': regdid,
            'af_radice_id': 1,
            'matricola_resp_did': '111111',
        })
        DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 2,
            'pds_regdid': pds,
            'des': 'informatica modulo 1',
            'af_gen_des_eng': 'computer science modulo 1',
            'ciclo_des': 'Secondo semestre',
            'regdid': regdid,
            'af_radice_id': 1,
        })
        DidatticaTestiAfUnitTest.create_didatticaTestiAf(**{
            'tipo_testo_af_cod': 'CONTENUTI',
            'testo_af_ita': 'Variabili',
            'testo_af_eng': 'Variables',
            'af': course,
        })
        p = PersonaleUnitTest.create_personale(**{
            'id': 1,
            'nome': 'Franco',
            'cd_ruolo': 'PO',
            'id_ab': 1,
            'matricola': '111111',
        })
        DidatticaCoperturaUnitTest.create_didatticaCopertura(**{
            'af': course,
            'personale': p,
        })

        url = reverse('ricerca:studyactivityinfo')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'studyactivityid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityID'] == 1

        data = {'studyactivityid': 1, 'language': 'eng'}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityContent'] == 'Variables'

        data = {'studyactivityid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['StudyActivityContent'] == 'Variabili'


class ApiCdSMainTeachersUnitTest(TestCase):

    def test_apicdsmainteachers(self):
        req = Client()

        regdid = DidatticaRegolamentoUnitTest.create_didatticaRegolamento()
        course1 = DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 1,
            'des': 'matematica',
            'af_gen_des_eng': 'math',
            'ciclo_des': 'Primo semestre',
            'regdid': regdid,
            'af_radice_id': 1,
        })
        course2 = DidatticaAttivitaFormativaUnitTest.create_didatticaAttivitaFormativa(**{
            'af_id': 2,
            'des': 'informatica',
            'af_gen_des_eng': 'computer science',
            'ciclo_des': 'Secondo semestre',
            'regdid': regdid,
            'af_radice_id': 2,
        })
        p1 = PersonaleUnitTest.create_personale(**{
            'id': 1,
            'nome': 'Simone',
            'cognome': 'Mungari',
            'cd_ruolo': 'PA',
            'id_ab': 1,
            'matricola': '111112',
        })
        p2 = PersonaleUnitTest.create_personale(**{
            'id': 2,
            'nome': 'Franco',
            'middle_name': 'Luigi',
            'cognome': 'Garofalo',
            'cd_ruolo': 'PO',
            'id_ab': 2,
            'matricola': '111111',
        })
        DidatticaCoperturaUnitTest.create_didatticaCopertura(**{
            'af': course1,
            'personale': p1,
        })
        DidatticaCoperturaUnitTest.create_didatticaCopertura(**{
            'af': course2,
            'personale': p2,
        })

        url = reverse('ricerca:cdsmainteachers')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['TeacherID'] == 1

        data = {'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['TeacherName'] == 'Mungari Simone'

        data = {'cdsid': 1}
        res = req.get(url, data=data)
        assert res.json()[
            'results'][1]['TeacherName'] == 'Garofalo Franco Luigi'


class ApiTeacherResearchGroupsUnitTest(TestCase):

    def test_apiteacherresearchgroups(self):
        req = Client()

        doc1 = PersonaleUnitTest.create_personale(**{
            'id': 1,
            'nome': 'Simone',
            'cognome': 'Mungari',
            'cd_ruolo': 'PA',
            'id_ab': 1,
            'matricola': '111112',
            'fl_docente': 1,
        })
        doc2 = PersonaleUnitTest.create_personale(**{
            'id': 2,
            'nome': 'Franco',
            'middle_name': 'Luigi',
            'cognome': 'Garofalo',
            'cd_ruolo': 'PO',
            'id_ab': 2,
            'matricola': '111111',
            'fl_docente': 1,
        })

        r1 = RicercaGruppoUnitTest.create_ricercaGruppo(**{
            'id': 1,
            'nome': 'Intelligenza Artificiale',
            'descrizione': 'ricerca su Machine Learning',
        })
        r2 = RicercaGruppoUnitTest.create_ricercaGruppo(**{
            'id': 2,
            'nome': 'Intelligenza Artificiale',
            'descrizione': 'ricerca su Deep Learning',
        })
        r3 = RicercaGruppoUnitTest.create_ricercaGruppo(**{
            'id': 3,
            'nome': 'Statistica',
            'descrizione': 'ricerca su Variabili Aleatorie',
        })

        RicercaDocenteGruppoUnitTest.create_ricercaDocenteGruppo(**{
            'personale': doc1,
            'ricerca_gruppo': r1,
            'id': 1,
        })
        RicercaDocenteGruppoUnitTest.create_ricercaDocenteGruppo(**{
            'personale': doc1,
            'ricerca_gruppo': r2,
            'id': 2,
        })
        RicercaDocenteGruppoUnitTest.create_ricercaDocenteGruppo(**{
            'personale': doc2,
            'ricerca_gruppo': r3,
            'id': 3,
            'dt_fine': '2021-01-03',
        })
        RicercaDocenteGruppoUnitTest.create_ricercaDocenteGruppo(**{
            'personale': doc2,
            'ricerca_gruppo': r2,
            'id': 4,
        })

        url = reverse('ricerca:teacherresearchgroups')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'teacherid': 1}
        res = req.get(url, data=data)
        assert res.json()['results'][0]['RGroupID'] == 1

        # two groups for teacherid = 1
        data = {'teacherid': 1}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 2

        # dt fine not null
        data = {'teacherid': 2}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 1


class ApiTeacherResearchLinesUnitTest(TestCase):

    def test_apiteacherresearchlinesunittest(self):
        req = Client()

        doc1 = PersonaleUnitTest.create_personale(**{
            'id': 1,
            'nome': 'Simone',
            'cognome': 'Mungari',
            'cd_ruolo': 'PA',
            'id_ab': 1,
            'matricola': '111112',
            'fl_docente': 1,
        })
        doc2 = PersonaleUnitTest.create_personale(**{
            'id': 2,
            'nome': 'Franco',
            'middle_name': 'Luigi',
            'cognome': 'Garofalo',
            'cd_ruolo': 'PO',
            'id_ab': 2,
            'matricola': '111111',
            'fl_docente': 1,
        })

        erc1 = RicercaErc1UnitTest.create_ricercaErc1(**{
            'cod_erc1': 'cod1_erc1',
            'descrizione': 'Computer Science and Informatics'
        })
        erc2 = RicercaErc2UnitTest.create_ricercaErc2(**{
            'cod_erc2': 'cod1_erc2',
            'descrizione': 'Machine learning',
            'ricerca_erc1': erc1
        })
        linea_base = RicercaLineaBaseUnitTest.create_ricercaLineaBase(**{
            'id': 1,
            'ricerca_erc2': erc2,
            'descrizione': 'regressione lineare',
            'descr_pubblicaz_prog_brevetto': 'pubblicazione 2020'
        })
        RicercaDocenteLineaBaseUnitTest.create_ricercaDocenteLineaBase(**{
            'personale': doc1,
            'ricerca_linea_base': linea_base
        })
        RicercaDocenteLineaBaseUnitTest.create_ricercaDocenteLineaBase(**{
            'personale': doc2,
            'ricerca_linea_base': linea_base,
            'dt_fine': '2021-01-03',
        })

        aster1 = RicercaAster1UnitTest.create_ricercaAster1(**{
            'id': 1,
            'descrizione': 'ICT & Design'
        })
        aster2 = RicercaAster2UnitTest.create_ricercaAster2(**{
            'id': 2,
            'descrizione': 'Algorithms. Data and signal processing',
            'ricerca_aster1': aster1
        })
        linea_applicata = RicercaLineaApplicataUnitTest.create_ricercaLineaApplicata(**{
            'id': 1,
            'ricerca_aster2': aster2,
            'descrizione': 'regressione lineare',
            'descr_pubblicaz_prog_brevetto': 'pubblicazione 2020'
        })
        linea_applicata2 = RicercaLineaApplicataUnitTest.create_ricercaLineaApplicata(**{
            'id': 2,
            'ricerca_aster2': aster2,
            'descrizione': 'random forest',
            'descr_pubblicaz_prog_brevetto': 'pubblicazione 2019'
        })
        RicercaDocenteLineaApplicataUnitTest.create_ricercaDocenteLineaApplicata(**{
            'personale': doc1,
            'ricerca_linea_applicata': linea_applicata,
            'dt_ins': '2021-01-03 15:47:21'
        })
        RicercaDocenteLineaApplicataUnitTest.create_ricercaDocenteLineaApplicata(**{
            'personale': doc1,
            'ricerca_linea_applicata': linea_applicata2,
            'dt_ins': '2021-01-03 15:47:21'
        })
        RicercaDocenteLineaApplicataUnitTest.create_ricercaDocenteLineaApplicata(**{
            'personale': doc2,
            'ricerca_linea_applicata': linea_applicata,
            'dt_ins': '2021-01-03 15:47:21'
        })

        url = reverse('ricerca:teacherresearchlines')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET

        data = {'teacherid': 1}
        res = req.get(url, data=data)
        assert res.json()[
            'results'][0]['R&SLineDescription'] == 'regressione lineare'

        data = {'teacherid': 1}
        res = req.get(url, data=data)
        print(res.json()['results'])
        assert len(res.json()['results']) == 3

        # teacherid 2 has one ricercalineabase (ended) and one
        # ricercalineaapplicata
        data = {'teacherid': 2}
        res = req.get(url, data=data)
        assert len(res.json()['results']) == 1

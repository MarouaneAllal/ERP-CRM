import csv
import random
import string
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_date():
    return datetime.strftime(datetime.today(), '%Y-%m-%d')

def generate_random_paragraphs():
    return '\n'.join(fake.paragraphs())

# Nombre de lignes à générer dans le fichier CSV
nombre_de_lignes = 10

# Nom du fichier CSV à créer
fichier_csv = 'donnees.csv'

# Ouvrir le fichier CSV en mode écriture
with open(fichier_csv, mode='w', newline='', encoding='utf-8') as csv_file:
    # Définir le séparateur comme point virgule
    csv_writer = csv.writer(csv_file, delimiter=';')

    # Écrire l'en-tête du fichier CSV
    csv_writer.writerow([
        'rowid', 'entity', 'ref_ext', 'ref_int', 'admin', 'employee',
        'fk_establishment', 'datec', 'tms', 'fk_user_creat', 'fk_user_modif',
        'login', 'pass_encoding', 'pass', 'pass_crypted', 'pass_temp',
        'api_key', 'gender', 'civility', 'lastname', 'firstname', 'address',
        'zip', 'town', 'fk_state', 'fk_country', 'birth', 'job',
        'office_phone', 'office_fax', 'user_mobile', 'personal_mobile',
        'email', 'personal_email', 'signature', 'socialnetworks', 'fk_soc',
        'fk_socpeople', 'fk_member', 'fk_user', 'fk_user_expense_validator',
        'fk_user_holiday_validator', 'idpers1', 'idpers2', 'idpers3',
        'note_public', 'note', 'model_pdf', 'datelastlogin',
        'datepreviouslogin', 'datelastpassvalidation', 'datestartvalidity',
        'dateendvalidity', 'iplastlogin', 'ippreviouslogin', 'egroupware_id',
        'ldap_sid', 'openid', 'statut', 'photo', 'lang', 'color', 'barcode',
        'fk_barcode_type', 'accountancy_code', 'nb_holiday', 'thm', 'tjm',
        'salary', 'salaryextra', 'dateemployment', 'dateemploymentend',
        'weeklyhours', 'import_key', 'default_range', 'default_c_exp_tax_cat',
        'fk_warehouse'
    ])

    # Générer des données aléatoires et les écrire dans le fichier CSV
    for _ in range(nombre_de_lignes):
        rowid = random.randint(100,10000)  # Générer un entier aléatoire entre 1000 et 99999 inclus
        entity = '1'
        ref_ext = 'NULL'
        ref_int = 'NULL'
        admin = random.choice(['0', '1'])
        employee = random.choice(['0', '1'])
        fk_establishment = '0'
        datec = 'NULL'
        tms = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        fk_user_creat = 'NULL'
        fk_user_modif = 'NULL'
        login = generate_random_string(5) + str(fake.random_int(100, 999))
        pass_encoding = 'NULL'
        pass_plain = generate_random_string(20)
        pass_crypted = 'NULL'
        pass_temp = 'NULL'
        api_key = 'NULL'
        gender = 'NULL'
        civility = 'NULL'
        lastname = fake.last_name()
        firstname = fake.first_name()
        address = fake.street_address()
        zip_code = fake.zipcode()
        town = fake.city()
        fk_state = '0'
        fk_country = '0'
        birth = generate_random_date()
        job = f"{fake.job()} at {fake.company()}"
        office_phone = fake.phone_number()
        office_fax = 'NULL'
        user_mobile = 'NULL'
        personal_mobile = 'NULL'
        email = f"{firstname.lower()}.{lastname.lower()}@{fake.domain_name()}"
        personal_email = f"{fake.user_name()}@{fake.domain_name()}"
        signature = 'NULL'
        socialnetworks = 'NULL'
        fk_soc = 'NULL'
        fk_socpeople = 'NULL'
        fk_member = 'NULL'
        fk_user = 'NULL'
        fk_user_expense_validator = 'NULL'
        fk_user_holiday_validator = 'NULL'
        idpers1 = 'NULL'
        idpers2 = 'NULL'
        idpers3 = 'NULL'
        note_public = 'NULL'
        note = 'NULL'
        model_pdf = 'NULL'
        datelastlogin = 'NULL'
        datepreviouslogin = 'NULL'
        datelastpassvalidation = 'NULL'
        datestartvalidity = 'NULL'
        dateendvalidity = 'NULL'
        iplastlogin = 'NULL'
        ippreviouslogin = 'NULL'
        egroupware_id = 'NULL'
        ldap_sid = 'NULL'
        openid = 'NULL'
        statut = '1'
        photo = 'NULL'
        lang = 'NULL'
        color = 'NULL'
        barcode = 'NULL'
        fk_barcode_type = '0'
        accountancy_code = 'NULL'
        nb_holiday = '0'
        thm = 'NULL'
        tjm = 'NULL'
        salary = 'NULL'
        salaryextra = 'NULL'
        dateemployment = 'NULL'
        dateemploymentend = 'NULL'
        weeklyhours = 'NULL'
        import_key = 'NULL'
        default_range = 'NULL'
        default_c_exp_tax_cat = 'NULL'
        fk_warehouse = 'NULL'

        csv_writer.writerow([
            rowid, entity, ref_ext, ref_int, admin, employee, fk_establishment,
            datec, tms, fk_user_creat, fk_user_modif, login, pass_encoding,
            pass_plain, pass_crypted, pass_temp, api_key, gender, civility,
            lastname, firstname, address, zip_code, town, fk_state, fk_country,
            birth, job, office_phone, office_fax, user_mobile, personal_mobile,
            email, personal_email, signature, socialnetworks, fk_soc,
            fk_socpeople, fk_member, fk_user, fk_user_expense_validator,
            fk_user_holiday_validator, idpers1, idpers2, idpers3, note_public,
            note, model_pdf, datelastlogin, datepreviouslogin,
            datelastpassvalidation, datestartvalidity, dateendvalidity,
            iplastlogin, ippreviouslogin, egroupware_id, ldap_sid, openid,
            statut, photo, lang, color, barcode, fk_barcode_type,
            accountancy_code, nb_holiday, thm, tjm, salary, salaryextra,
            dateemployment, dateemploymentend, weeklyhours, import_key,
            default_range, default_c_exp_tax_cat, fk_warehouse
        ])

print(f"Fichier CSV '{fichier_csv}' généré avec succès.")


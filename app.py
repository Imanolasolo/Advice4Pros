import streamlit as st
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# Configuración de la página
st.set_page_config(page_title="Technical advice Management", page_icon=":coffee:", layout="centered")

st.title("Technical Advice Management for Pros")
st.info("Welcome to the tech tips management app, Follow the next instructions to receive advice on any technical questions you may have.")
st.error("Do you have any questions at a technical level and want to resolve them through a specialized technician? This is the app where you can get advice aimed at managing your projects provided by proven professionals.")
st.warning("Please make payment of advice at Buy Me a Coffee to access (1 coffee for advice).") 

# Campos de entrada para el usuario
coffee_url = "https://www.buymeacoffee.com/imanolasolo"  # Reemplaza con tu URL de Buy Me a Coffee
st.markdown(f"[Make payment]({coffee_url})")

payment_code = st.text_input("Enter the payment code provided by Buy Me a Coffee:")
user_name = st.text_input("Name:")
user_email = st.text_input("Email:")
advice_request = st.text_area("Describe your request for advice:")

# Función para verificar el pago
def verificar_pago(payment_code):
    url = f"https://www.buymeacoffee.com/api/v1/payments/{payment_code}"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5MTI5ZDIwMC1kYTdkLTRjY2MtOWQzZC01ODA0MTU0ZTgyMjYiLCJqdGkiOiJhYjczOWZmYjU2NDIyYzVjOTIxMmM1OTkxMzc2MzE5Yzk5ODY3YTY4YzM0MDJlZGVmY2E5NWE3ZTkxNTA2MGFmN2RjYjViZDhmNDhiMGNkYyIsImlhdCI6MTcxOTA3MTE3MywibmJmIjoxNzE5MDcxMTczLCJleHAiOjE3MzQ4ODIzNzIsInN1YiI6IjI4NjY0MzAiLCJzY29wZXMiOlsicmVhZC1vbmx5Il19.CuR6wQ1uTM1sVH3j38Aozi_eiryEUwMfj4gWLuPHC-_2qFrM-8vXClHR1X8V0ZKDFQNDWZGwpcRRb9R4j9DtVteFAalUxzZ5kXgANHh_lAnGdyn5mDzb4FnAMBX0VMBkVQIAF4pJROwdjZG6EC7zBuMeK3F5_xH7WFfVJ7C1_1mPoKApR2pBU8GqW3YByZKiUwwVOlHBFEjxCv0FSIUH9cCOAzzrejxBGAGPW3fvMztj-uPZ5zSP3saxMnNHO6siyV-sfk8iCC36iXatsmsVp3jXrLrba97i9Cue_2Ja24AsFr3azWhsJDEa3JEkBmHww9n4jzzk81wdUK8XvxVA1z6dixSPEjVSMb13rpyMJkVEa7rhEnB7mITXROhyo_FfanrtynuzpeKH76aPLw065iOHRp_mWUUxKia8BI0JHQejizTzOACYvSCKWhr3T4Lo-__Ej2NEebxFGHdCBfReS_wANsq4AZbN3bedXoaW2wzIZYf8t-rqHXPl5b5gqzHeM8kfqW1WDkfXw2Vj1xu9-GZ7ufPRurcJ_Ji2iEukaV7C6lRqga5jnDVRzL9OhhH5DUvfDrS1lFtLg9n_kqomQafNxXjV4mgw4vF-YsrpNoUQAFu65rN162P2F-Kl2OU0q2KgDEwZy2X1CqdL97hVfBcVn1cOIT87pfZh2pr_gpg"  # Reemplaza con tu token de API
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

# Función para generar enlace de WhatsApp
def generar_enlace_whatsapp(mensaje, numero):
    mensaje_encoded = requests.utils.quote(mensaje)
    enlace = f"https://wa.me/{numero}?text={mensaje_encoded}"
    return enlace

# Función para enviar correo electrónico
def enviar_correo(destinatario, asunto, mensaje):
    remitente = "jjusturi@gmail.com"
    contraseña = "egmt eunc uuch hhcf"
    
    msg = MIMEText(mensaje, "plain", "utf-8")
    msg["Subject"] = Header(asunto, "utf-8")
    msg["From"] = formataddr((str(Header("Remitente", "utf-8")), remitente))
    msg["To"] = destinatario
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(remitente, contraseña)
        server.sendmail(remitente, destinatario, msg.as_string())

# Integrar en la aplicación
if st.button("Send request"):
    if verificar_pago(payment_code):
        st.success("Verified payment. Sending request...")
        mensaje = f"Nombre: {user_name}\nCorreo: {user_email}\nPetición: {advice_request}"
        
        try:
            # Generar enlace de WhatsApp
            enlace_whatsapp = generar_enlace_whatsapp(mensaje, '+5930993513082')
            st.markdown(f"[Click here to send your request via WhatsApp]({enlace_whatsapp})")
            
            # Enviar correo electrónico
            enviar_correo('jjusturi@gmail.com', 'Nueva Petición de Consejo', mensaje)
            st.info("Request sent by email successfully.")
        
        except Exception as e:
            st.error(f"Error sending request: {e}")
        
    else:
        st.error("Invalid payment code. Please verify and try again.")

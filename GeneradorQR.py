import qrcode
import streamlit as st
from io import BytesIO

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Usar un buffer de bytes en lugar de guardar la imagen en el disco
    buf = BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

# Crear la aplicación en Streamlit
st.set_page_config(page_title="Generador de código QR", page_icon="🌐", layout="centered")
#st.image("images/supports.JPG", use_column_width=True)
st.title("Generador de código QR")

url = st.text_input("Ingresar la URL")

if st.button("Generar QR") and url:
    img_buffer = generate_qr_code(url)
    st.image(img_buffer, use_column_width=True)
    img_buffer.seek(0)  # Regresar al inicio del buffer para la descarga
    st.download_button(label="Descargar QR", data=img_buffer, file_name="qr_generated.png", mime="image/png")
    st.success("QR generado ok!")
else:
    st.error("Ingrese una URL válida")



# Pie de página con enlace a LinkedIn
st.markdown("""
---
#### Desarrollado por [Luis Ponce de León](https://www.linkedin.com/in/jponcedeleon/)
Sígueme en [LinkedIn](https://www.linkedin.com/in/jponcedeleon/) para más proyectos como este.
""", unsafe_allow_html=True)

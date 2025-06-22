# Microservicio de Notificaciones - Funeraria Digital

Este microservicio es responsable de gestionar y enviar todas las notificaciones a los usuarios del sistema, incluyendo correos electrónicos y mensajes de texto (SMS). Está construido con Flask y se integra con los servicios de AWS (Amazon Web Services) para el envío de las notificaciones.

## Tabla de Contenidos

1.  [Descripción General](#descripción-general)
2.  [Características](#características)
3.  [Endpoints de la API](#endpoints-de-la-api)
4.  [Configuración](#configuración)
5.  [Instalación y Ejecución](#instalación-y-ejecución)

## Descripción General

El microservicio de notificaciones centraliza la comunicación saliente del sistema funerario. Utiliza los siguientes servicios de AWS:

* **Amazon Simple Notification Service (SNS):** Para el envío de mensajes de texto (SMS) a los números de teléfono de los usuarios.
* **Amazon Simple Email Service (SES):** Para el envío de correos electrónicos utilizando plantillas predefinidas.

El servicio está diseñado para ser consumido por otros microservicios que necesiten notificar a los usuarios, como el envío de códigos de doble factor de autenticación (2FA) o la confirmación de registros.

## Características

* **Envío de SMS:** Proporciona endpoints para el envío de mensajes de texto.
* **Envío de Correos Electrónicos:** Permite el envío de correos electrónicos basados en plantillas HTML de AWS SES.
* **Integración con AWS:** Utiliza `boto3`, el SDK de AWS para Python, para comunicarse con los servicios de SNS y SES.
* **Configuración Flexible:** Carga las credenciales de AWS y otras configuraciones desde variables de entorno.

## Endpoints de la API

El microservicio expone los siguientes endpoints para el envío de notificaciones:

### SMS

* `POST /sms`
    * Envía un mensaje de texto genérico.
    * **Payload (JSON):**
        ```json
        {
          "destination": "NUMERO_DE_TELEFONO_DESTINO",
          "message": "CONTENIDO_DEL_MENSAJE"
        }
        ```

* `POST /sms-2fa`
    * Envía un mensaje de texto formateado para 2FA, incluyendo el nombre del usuario.
    * **Payload (JSON):**
        ```json
        {
          "destination": "NUMERO_DE_TELEFONO_DESTINO",
          "name": "NOMBRE_DEL_USUARIO",
          "message": "CONTENIDO_DEL_MENSAJE"
        }
        ```

### Correo Electrónico

* `POST /email`
    * Envía un correo electrónico utilizando la plantilla `AWS-SES-Email-Without-Name`.
    * **Payload (JSON):**
        ```json
        {
          "destination": "CORREO_DESTINO",
          "subject": "ASUNTO_DEL_CORREO",
          "message": "CONTENIDO_DEL_MENSAJE"
        }
        ```

* `POST /email-2fa`
    * Envía un correo electrónico utilizando la plantilla `AWS-SES-Email-With-Name`, que incluye el nombre del usuario.
    * **Payload (JSON):**
        ```json
        {
          "destination": "CORREO_DESTINO",
          "name": "NOMBRE_DEL_USUARIO",
          "subject": "ASUNTO_DEL_CORREO",
          "message": "CONTENIDO_DEL_MENSAJE"
        }
        ```

## Configuración

### Plantillas de AWS SES

El servicio utiliza plantillas de correo electrónico predefinidas en AWS SES para asegurar un formato consistente. Las plantillas utilizadas son:

* `AWS-SES-Email-Without-Name`: Una plantilla genérica.
* `AWS-SES-Email-With-Name`: Una plantilla que incluye un saludo personalizado con el nombre del destinatario.

### Variables de Entorno

Para su correcto funcionamiento, el microservicio requiere la configuración de las siguientes variables de entorno en un archivo `.env` en la raíz del proyecto:

* `AWS_ACCESS_KEY_ID:` Tu clave de acceso de AWS.
* `AWS_SECRET_ACCESS_KEY:` Tu clave de acceso secreta de AWS.
* `AWS_REGION:` La región de AWS donde están configurados tus servicios de SNS y SES (ej. `us-east-1`).

## Instalación y Ejecución

Para instalar y ejecutar el microservicio, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/cruz1122/ms-notificaciones-funeraria.2024.git](https://github.com/cruz1122/ms-notificaciones-funeraria.2024.git)
    cd ms-notificaciones-funeraria.2024
    ```

2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install Flask python-dotenv boto3
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto y añade las credenciales de AWS.

5.  **Ejecutar el microservicio:**
    ```bash
    python server.py
    ```

El microservicio estará disponible en `http://127.0.0.1:5000`.

from openai import OpenAI
import streamlit as st
import speech_recognition as sr


# def process_messages(in_prompt, role, session_state, in_client):
#     if 'message_thread' not in session_state:
#         session_state['message_thread'] = in_client.beta.threads.create()
#
#     message_create = client.beta.threads.messages.create(
#         thread_id=session_state.message_thread.id,
#         role="user",
#         content=in_prompt,
#     )
#
#     if "messages" not in session_state:
#         session_state.messages = []
#
#     for message in session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])
#
#     session_state.messages.append({"role": role, "content": in_prompt})
#
#     with st.chat_message(role):
#         st.markdown(in_prompt)
#
#     if role == "user":
#         msg = ""
#
#         with in_client.beta.threads.runs.stream(
#                 thread_id=session_state.message_thread.id,
#                 assistant_id=session_state['assistant_id']
#         ) as stream:
#             for event in stream:
#                 # Print the text from text delta events
#                 if event.event == "thread.message.delta" and event.data.delta.content:
#                     msg = msg + str(event.data.delta.content[0].text.value)
#         response = st.write(msg)
#         session_state.messages.append({"role": "assistant", "content": response})
#
#     return session_state
#


# client = OpenAI(api_key=st.secrets.OPENAI_API_KEY)
#
# # Define a dictionary to map each selection to an assistant id and corresponding message
# selection_actions = {
#     'Lead Magnet':
#         {'assistant_id': st.secrets.assistant_id_1, 'message': 'Creating Lead Magnet...'},
#     'Funnel MARATHON / WEBINAR':
#         {'assistant_id': st.secrets.assistant_id_2, 'message': 'Creating WEBINAR...'},
#     'Warm-up plan for the product for 5 days':
#         {'assistant_id': st.secrets.assistant_id_3, 'message': 'Creating Warm-up plan...'},
#     'Sites':
#         {'assistant_id': st.secrets.assistant_id_4, 'message': 'Creating Sites...'},
#     'Storyteller':
#         {'assistant_id': st.secrets.assistant_id_5, 'message': 'Creating Storyteller...'},
# }

# add_selectbox = st.sidebar.selectbox('What would you like to create?', selection_actions)
#
# if add_selectbox in selection_actions:
#     st.sidebar.markdown("# Fill in the fields")
#     text_input1 = st.sidebar.text_area("Product Data")
#     text_input2 = st.sidebar.text_area("Target Audience Data")
#
#     st.write(selection_actions[add_selectbox]['message'])
#
#     st.session_state['assistant_id'] = selection_actions[add_selectbox]['assistant_id']
#
#     # ... omitted for brevity
#     prompt = f"Product Data: {text_input1}, Target Audience Data: {text_input2}"
#     if st.sidebar.button('START'):
#         st.session_state = process_messages(prompt, "user", st.session_state, client)
#
#     # ... omitted for brevity
#     if prompt := st.chat_input("What is up?"):
#         st.session_state = process_messages(prompt, "user", st.session_state, client)

if st.sidebar.button("Записать аудио"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Говорите что-нибудь...")
        audio = recognizer.listen(source)
        st.write("Аудио записано!")

        # Транскрибация аудио
        try:
            text = recognizer.recognize_google_cloud(
                audio,
                credentials_json=st.secrets.GOOGLE_CLOUD_SPEECH_CREDENTIALS,
                language="ru-RU",)
            # text = recognizer.recognize_google(audio, language="ru-RU")
            st.write("Транскрибированный текст:")
            text_input1 = st.write(text)
        except sr.UnknownValueError:
            st.write("Не удалось распознать аудио")
        except sr.RequestError as e:
            st.write(f"Ошибка службы распознавания: {e}")

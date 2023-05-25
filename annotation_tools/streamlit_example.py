import os
import random

import streamlit as st


def show():
    st.write(
        """
        ## 📚 Text Annotation

        Welcome to the text annotation tool! Label some text and all of your
        annotations will be preserved in `st.session_state`!
        """
    )

    data = [
        "I love this movie! It's so entertaining.",
        "This book is boring and poorly written.",
        "The food at that restaurant was delicious.",
        "I had a terrible experience with their customer service.",
        "The weather today is perfect for outdoor activities.",
    ]

    if "annotations" not in st.session_state:
        st.session_state.annotations = {}
        st.session_state.data = data.copy()
        st.session_state.current_text = data[0]

    def annotate(label):
        st.session_state.annotations[st.session_state.current_text] = label
        if st.session_state.data:
            st.session_state.current_text = random.choice(st.session_state.data)
            st.session_state.data.remove(st.session_state.current_text)

    st.write("")
    col1, col2 = st.beta_columns(2)
    with col1:
        if st.session_state.data:
            st.write(
                "Annotated:",
                len(st.session_state.annotations),
                "– Remaining:",
                len(st.session_state.data),
            )
            st.write("### Text")
            st.write(st.session_state.current_text)
            st.button("Positive 😄", on_click=annotate, args=("positive",))
            st.button("Negative 😞", on_click=annotate, args=("negative",))
            st.button("Neutral 😐", on_click=annotate, args=("neutral",))
        else:
            st.success(
                f"🎉 Done! All {len(st.session_state.annotations)} texts annotated."
            )
    with col2:
        st.write("### Annotations")
        st.write(st.session_state.annotations)


if __name__ == "__main__":
    show()

import streamlit as st
import pandas as pd
import annotate

# Load the press release data into a Pandas DataFrame
df = pd.read_csv("https://raw.githubusercontent.com/hoyinli1211/NER_ICAC/main/ICACPressReleases.csv")

st.title("Named Entity Annotation Tool")

# Display the text of the press release
text_input = st.text_area("Press Release Text", df.iloc[0]["text"])

# Add buttons for labeling named entities
person_button = st.button("Person")
organization_button = st.button("Organization")
location_button = st.button("Location")

# Save the annotated data
if person_button or organization_button or location_button:
  # Create an AnnoTate annotation document
  doc = annotate.Document(text=text_input)

  # Add the annotated data to the document
  doc.add_entities(ner.extract_entities(text_input))

  # Save the document
  doc.save("icac_ner.jsonl")
  st.write("Annotated data saved!")

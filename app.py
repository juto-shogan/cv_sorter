import streamlit as st
import tempfile
import os

from main import (
    read_cv,
    get_file_type,
    determine_role,
    cv_checker,
    grader,
    manual_check,
    supported_extensions,
    profession_keywords,
)

st.set_page_config(page_title="CV Analyzer", layout="centered")

st.title("📄 AI CV Analyzer")
st.markdown("Upload your CV and get matched to a profession with tailored feedback.")

mode = st.radio("Choose Analysis Mode:", ("Automatic", "Manual"))

if mode == "Automatic":
    uploaded_file = st.file_uploader("Upload your CV (.docx, .pdf, .txt)", type=["docx", "pdf", "txt"])

    if uploaded_file:
        # Save to a temp file for reading
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        st.success("✅ File uploaded successfully!")

        file_type = get_file_type(tmp_path, supported_extensions)
        content = read_cv(tmp_path)

        if content:
            best_role, role_details = determine_role(content)
            if best_role:
                st.subheader("🔍 Role Recommendation")
                st.write(f"**Recommended Role:** {best_role.replace('_', ' ').title()}")
                
                count, matched_keywords = cv_checker(content, role_details['keywords'])
                
                st.subheader("📊 Keyword Match")
                st.write(f"**Matched Keywords:** {count} / {len(role_details['keywords'])}")
                st.write("✅ " + ", ".join(matched_keywords))

                st.subheader("📈 Evaluation")
                if len(role_details['keywords']) / 2 > count:
                    st.error("Grade: ❌ Failed")
                elif len(role_details['keywords']) == count:
                    st.success("Grade: ✅ Passed")
                else:
                    st.warning("Grade: ⚠️ Under Consideration")

                st.subheader("💡 Career Advice")
                st.write("**Experience Levels:**", ", ".join(role_details['experience_levels']))
                st.write("**Related Roles:**", ", ".join(role_details['related_roles']))
                st.write("**Potential Needs:**", ", ".join(role_details['potential_needs']))
            else:
                st.warning("No suitable role found.")
        else:
            st.error("Could not read content from the file.")

elif mode == "Manual":
    job_list = {
        'software developer': 'Software Developer',
        'data scientist': 'Data Scientist',
        'customer service': 'Customer Service',
        'cyber security': 'Cyber Security'
    }

    selected_role = st.selectbox("Select the role you're applying for:", list(job_list.keys()))
    user_skills = st.text_input("Enter your skills (comma-separated):")

    if st.button("Analyze Skills"):
        if selected_role and user_skills:
            keywords = profession_keywords[selected_role.replace(' ', '_') + '_keywords']['keywords']
            skill_list = [skill.strip().lower() for skill in user_skills.split(",")]
            matched_skills = [skill for skill in skill_list if skill in keywords]

            st.write("✅ **Matched Skills:**", ", ".join(matched_skills) if matched_skills else "None")
            st.write(f"You matched {len(matched_skills)} skill(s) out of {len(keywords)} for the **{job_list[selected_role]}** role.")

            role_details = profession_keywords[selected_role.replace(' ', '_') + '_keywords']
            st.subheader("💡 Career Advice")
            st.write("**Experience Levels:**", ", ".join(role_details['experience_levels']))
            st.write("**Related Roles:**", ", ".join(role_details['related_roles']))
            st.write("**Potential Needs:**", ", ".join(role_details['potential_needs']))
        else:
            st.warning("Please select a role and enter your skills.")

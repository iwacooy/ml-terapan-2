import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
import io

# Buffer untuk simpan file excel hasil prediksi (jika perlu ekspor)
excel_buffer = io.BytesIO()

def preprocess_input(data, is_single, count):
    ref_data = pd.read_csv('data_selected.csv')
    ref_data.drop('Status', axis=1, inplace=True)
    combined = pd.concat([data, ref_data], ignore_index=True)
    scaled = StandardScaler().fit_transform(combined)
    return scaled[[count]] if is_single else scaled[:count]

def predict_student_status(features):
    rf_model = joblib.load('model_rf_param.joblib')
    return rf_model.predict(features)

def highlight_status(cell_value):
    return 'color: green; font-weight: bold' if cell_value == 'Graduate' else 'color: red; font-weight: bold'

def run_app():
    st.title('🎓 Student Outcome Predictor - Jaya Jaya Institute')

    # Mapping kategori
    gender_map = {'Male': 1, 'Female': 0}
    marital_map = {
        'Single': 1, 'Married': 2, 'Widower': 3, 'Divorced': 4,
        'Facto Union': 5, 'Legally Seperated': 6
    }
    application_map = {
        '1st Phase - General Contingent': 1,
        '2nd Phase - General Contingent': 17,
        '3rd Phase - General Contingent': 18,
        'Ordinance No. 612/93': 2,
        'Over 23 Years Old': 39,
        'Transfer': 42,
        'Change of Course': 43,
        'International Student (Bachelor)': 15,
    }

    with st.form('single_student_form'):
        g = st.radio('Select Gender', options=['Male', 'Female'])
        a = st.slider('Age at Enrollment', 17, 70, 18)
        m = st.selectbox('Marital Status', list(marital_map.keys()))
        app_mode = st.selectbox('Application Mode', list(application_map.keys()))

        prev_grade = st.slider('Previous Qualification Grade', 0, 200, 150)
        adm_grade = st.slider('Admission Grade', 0, 200, 150)

        scholarship = st.checkbox('Scholarship Holder')
        tuition = st.checkbox('Tuition Fees Up to Date')
        displaced = st.checkbox('Displaced Person')
        debtor = st.checkbox('Debtor')

        cu_1_enrolled = st.slider('Units 1st Sem Enrolled', 0, 26, 10)
        cu_1_approved = st.slider('Units 1st Sem Approved', 0, 26, 8)
        cu_1_grade = st.slider('Units 1st Sem Grade', 0, 20, 14)

        cu_2_enrolled = st.slider('Units 2nd Sem Enrolled', 0, 23, 10)
        cu_2_eval = st.slider('Units 2nd Sem Evaluations', 0, 33, 12)
        cu_2_approved = st.slider('Units 2nd Sem Approved', 0, 20, 10)
        cu_2_grade = st.slider('Units 2nd Sem Grade', 0, 20, 14)
        cu_2_no_eval = st.slider('Units 2nd Sem No Evaluations', 0, 12, 1)

        submit_btn = st.form_submit_button('Predict')

    if submit_btn:
        single_df = pd.DataFrame([[  # Dataframe 1 baris
            marital_map[m],
            application_map[app_mode],
            prev_grade,
            adm_grade,
            int(displaced),
            int(debtor),
            int(tuition),
            gender_map[g],
            int(scholarship),
            a,
            cu_1_enrolled,
            cu_1_approved,
            cu_1_grade,
            cu_2_enrolled,
            cu_2_eval,
            cu_2_approved,
            cu_2_grade,
            cu_2_no_eval
        ]], columns=[
            'Marital_status', 'Application_mode', 'Previous_qualification_grade', 'Admission_grade',
            'Displaced', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
            'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
            'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
            'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations'
        ])

        processed = preprocess_input(single_df, True, 0)
        pred = predict_student_status(processed)

        if pred[0] == 1:
            st.success('✅ Prediction: The student is likely to **Graduate** 🎓')
        else:
            st.error('⚠️ Prediction: The student is likely to **Dropout**')

if __name__ == '__main__':
    run_app()

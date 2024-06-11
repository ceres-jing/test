import streamlit as st

# Function to display IT policies in a card format
def display_policy_card(title, content):
    st.markdown(f"""
    <div style="background-color: white; padding: 20px; border: 1px solid #ddd; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: 10px;">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# Function to display the main content
def main():

    st.markdown("""
    <style>
    .policy-card {
        background-color: white;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        margin: 10px;
        width: calc(100% - 40px);
        height: 200px; /* Adjust height as needed */
        display: inline-block;
        vertical-align: top;
    }
    .policy-card h3 {
        margin-top: 0;
    }
    .policy-card p {
        margin: 0;
        text-align: justify; /* Align text consistently */
    }
    </style>
    """, unsafe_allow_html=True)
    st.title("Bank IT Policy Classes")

    # Navigation bar
    with st.container():
        nav = st.selectbox("Navigate to", ("Security Policy", "Data Backup Policy", "Access Control Policy", "Incident Response Policy"))

    # Display different policy sections based on navigation
    if nav == "Security Policy":
        st.header("Security Policy")
        display_policy_card("Security Policy", """
        - Ensure data confidentiality
        - Implement strong authentication mechanisms
        - Regular security audits and compliance checks
        """)
    elif nav == "Data Backup Policy":
        st.header("Data Backup Policy")
        display_policy_card("Data Backup Policy", """
        - Daily incremental backups
        - Weekly full backups
        - Secure offsite storage for backups
        """)
    elif nav == "Access Control Policy":
        st.header("Access Control Policy")
        display_policy_card("Access Control Policy", """
        - Role-based access control
        - Regular review of access permissions
        - Multi-factor authentication for sensitive data
        """)
    elif nav == "Incident Response Policy":
        st.header("Incident Response Policy")
        display_policy_card("Incident Response Policy", """
        - Immediate reporting of security incidents
        - Pre-defined incident response team
        - Regular incident response drills and training
        """)

    # Display horizontally parallel sections
    st.write("## Policies Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        display_policy_card("Security Policy", "Ensure data confidentiality and implement strong authentication mechanisms.")

    with col2:
        display_policy_card("Data Backup Policy", "Daily incremental backups and weekly full backups with secure offsite storage.")

    with col3:
        display_policy_card("Access Control Policy", "Role-based access control and regular review of access permissions.")

    with col4:
        display_policy_card("Incident Response Policy", "Immediate reporting of security incidents and pre-defined incident response team.")

if __name__ == "__main__":
    main()

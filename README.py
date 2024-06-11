import streamlit as st

# Function to display IT policies in a card format
def display_policy_card(title, content, anchor):
    st.markdown(f"""
    <div id="{anchor}" style="background-color: white; padding: 20px; border: 1px solid #ddd; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: 10px;">
        <h3>{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

# Main function
def main():
    st.title("Bank IT Policy Classes")

    # Navigation bar
    st.markdown("""
    <nav style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
        <a href="#security-policy" style="margin-right: 10px;">Security Policy</a>
        <a href="#data-backup-policy" style="margin-right: 10px;">Data Backup Policy</a>
        <a href="#access-control-policy" style="margin-right: 10px;">Access Control Policy</a>
        <a href="#incident-response-policy" style="margin-right: 10px;">Incident Response Policy</a>
    </nav>
    """, unsafe_allow_html=True)

    # Display different policy sections based on navigation
    st.header("Security Policy")
    display_policy_card("Security Policy", """
    - Ensure data confidentiality
    - Implement strong authentication mechanisms
    - Regular security audits and compliance checks
    """, "security-policy")

    st.header("Data Backup Policy")
    display_policy_card("Data Backup Policy", """
    - Daily incremental backups
    - Weekly full backups
    - Secure offsite storage for backups
    """, "data-backup-policy")

    st.header("Access Control Policy")
    display_policy_card("Access Control Policy", """
    - Role-based access control
    - Regular review of access permissions
    - Multi-factor authentication for sensitive data
    """, "access-control-policy")

    st.header("Incident Response Policy")
    display_policy_card("Incident Response Policy", """
    - Immediate reporting of security incidents
    - Pre-defined incident response team
    - Regular incident response drills and training
    """, "incident-response-policy")

    # Display horizontally parallel sections
    st.write("## Policies Overview")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        display_policy_card("Security Policy", "Ensure data confidentiality and implement strong authentication mechanisms.", "security-policy")

    with col2:
        display_policy_card("Data Backup Policy", "Daily incremental backups and weekly full backups with secure offsite storage.", "data-backup-policy")

    with col3:
        display_policy_card("Access Control Policy", "Role-based access control and regular review of access permissions.", "access-control-policy")

    with col4:
        display_policy_card("Incident Response Policy", "Immediate reporting of security incidents and pre-defined incident response team.", "incident-response-policy")

if __name__ == "__main__":
    main()

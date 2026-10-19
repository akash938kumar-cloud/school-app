import streamlit as st

# Page Configuration (Title and Icon)
st.set_page_config(page_title="Smart Student Hub 🏫", page_icon="🎓", layout="centered")

# Custom Title Block
st.title("🏫 Smart Student Learning & Utility App")
st.write("A simple and fun tool for your classroom calculations and learning! ✨")

# Sidebar Menu
st.sidebar.header("🎯 Select Topic")
choice = st.sidebar.radio("What would you like to calculate?", [
    "📐 Area & Perimeter Calculator", 
    "📊 Student Percentage & Grade", 
    "🔢 Fun Math Tables"
])

st.divider()

# -------------------------------------------------------------
# 1. AREA CALCULATOR
# -------------------------------------------------------------
if choice == "📐 Area & Perimeter Calculator":
    st.header("📐 Area & Perimeter Calculator")
    st.info("Calculate the area and boundary of a room, playground, or rectangle shape.")
    
    col1, col2 = st.columns(2)
    with col1:
        length = st.number_input("Length (in feet/meters):", min_value=0.0, value=15.0, step=1.0)
    with col2:
        width = st.number_input("Width (in feet/meters):", min_value=0.0, value=10.0, step=1.0)
    
    if st.button("Calculate Area & Perimeter 🚀"):
        area = length * width
        perimeter = 2 * (length + width)
        
        st.success(f"📌 *Total Area:* {area} sq. units")
        st.info(f"📏 *Total Perimeter (Boundary):* {perimeter} units")
        
        st.balloons()
        st.write(f"💡 *Real Life Use:* To install tiles in this room, you will need *{area} sq. units* of tiles!")

# -------------------------------------------------------------
# 2. PERCENTAGE & GRADE CHECKER
# -------------------------------------------------------------
elif choice == "📊 Student Percentage & Grade":
    st.header("📊 Percentage & Grade Calculator")
    st.info("Enter your obtained marks and total marks to calculate percentage and grade.")
    
    col1, col2 = st.columns(2)
    with col1:
        obtained = st.number_input("Marks Obtained:", min_value=0.0, value=450.0, step=5.0)
    with col2:
        total = st.number_input("Total Marks:", min_value=1.0, value=600.0, step=5.0)
    
    if st.button("Check Result & Grade 🎉"):
        if obtained > total:
            st.error("Marks Obtained cannot be greater than Total Marks!")
        else:
            percentage = (obtained / total) * 100
            st.success(f"🎯 *Your Percentage:* {percentage:.2f}%")
            
            # Grade Calculation
            if percentage >= 90:
                st.balloons()
                st.subheader("Grade: A+ 🌟 (Outstanding!)")
            elif percentage >= 75:
                st.subheader("Grade: A 🎉 (Excellent!)")
            elif percentage >= 60:
                st.subheader("Grade: B 👍 (Very Good!)")
            elif percentage >= 33:
                st.subheader("Grade: C 😃 (Passed!)")
            else:
                st.error("Grade: Needs Improvement 💪 (Keep working hard!)")

# -------------------------------------------------------------
# 3. MATH TABLES
# -------------------------------------------------------------
elif choice == "🔢 Fun Math Tables":
    st.header("🔢 Interactive Math Table Generator")
    st.info("Generate the multiplication table for any number instantly!")
    
    num = st.number_input("Enter the number for the table:", min_value=1, max_value=100, value=7, step=1)
    
    if st.button(f"Generate Table of {num} ✨"):
        st.subheader(f"📖 Table of {num}:")
        for i in range(1, 11):
            st.write(f"👉 *{num} × {i} = {num * i}*")

st.divider()
st.caption("Designed with ❤️ for School Students using Python & Streamlit")

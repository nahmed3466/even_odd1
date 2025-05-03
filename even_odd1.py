import streamlit as st

class EvenOddCheckerApp:
    """A Streamlit app to check if numbers are even or odd."""

    def check_number(self, num):
        """Check if a number is even or odd."""
        if num % 2 == 0:
            return f"The number {num} is even."
        else:
            return f"The number {num} is odd."

    def run(self):
        """Run the Streamlit app."""
        st.title("Even or Odd Checker")
        st.write("Enter a number below to check if it's even or odd.")

        # Input for the number
        user_input = st.text_input("Enter a number:")

        if user_input:
            try:
                # Convert input to integer and check
                num = int(user_input)
                result = self.check_number(num)
                st.success(result)
            except ValueError:
                st.error("Invalid input. Please enter a valid integer.")

# Instantiate and run the app
if __name__ == "__main__":
    app = EvenOddCheckerApp()
    app.run()

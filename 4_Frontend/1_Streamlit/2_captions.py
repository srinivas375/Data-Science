import streamlit as st

# captions
st.caption("This is a sample caption")

#latex
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")

# json
json = {"name":"boby", "role": "engineer"}
st.json(json)

# code display

code = """
print("Welcome to python")
def func(value):
    new = value
    new += 99
    return new, value
"""
code_2 = """
int main()
{
    int val = 0;
    float next = 99.7;
    char[9] name;
    int *ptr = &val;
    printf("%d", ptr);
    return 0;
}
"""
st.code(code, language="python")
st.code(code_2, language="c")
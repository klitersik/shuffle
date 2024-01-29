import streamlit as st
import pandas as pd
import random

# Lista dostępnych klas
CLASSES = ['top', 'jungle', 'mid', 'adc', 'supp']
CLASSES2 = ['top', 'jungle', 'mid', 'adc', 'supp']
CLASSES3 = ['top', 'jungle', 'mid', 'adc', 'supp']

def create_dataframes(names):
    # Podział nazw na listę
    names_list = [name.strip() for name in names.split(',')]

    # Losowanie połowy nazw do każdego DataFrame
    half_length = len(names_list) // 2
    random.shuffle(names_list)

    random.shuffle(CLASSES)
    random.shuffle(CLASSES2)

    names_df1 = names_list[:half_length]
    names_df2 = names_list[half_length:]

    # Losowanie klas dla każdego DataFrame
    class_df1 = []
    class_df2 = []

    # Tworzenie DataFrame'ów
    df1 = pd.DataFrame({'Nick': names_df1})
    df2 = pd.DataFrame({'Nick': names_df2})

    df1['rola'] = CLASSES[:len(df1)]
    df2['rola'] = CLASSES2[:len(df2)]

    return df1, df2

def main():
    st.write('Wprowadź nazwy oddzielone przecinkiem, aby utworzyć drużyny np.')
    st.write("maciek, emil, jakub, ala, mirek, marek, filip, dawid, michał, borys")

    # Pole do wprowadzania danych
    names_input = st.text_input('Wprowadź nazwy:', '')

    if st.button('Utwórz Drużyny'):
        col1, col2 = st.columns(2)

        if names_input:
            df1, df2 = create_dataframes(names_input)
            with col1:
                st.write('TEAM 1:')
                df1['rola'] = pd.Categorical(df1['rola'], categories=CLASSES3, ordered=True)
                df1 = df1.sort_values(by='rola')
                st.table(df1.style.set_table_styles([{
                    'selector': 'table',
                    'props': [
                        ('font-size', '25px')
                    ]
                }]))
            with col2:
                st.write('TEAM 2:')
                df2['rola'] = pd.Categorical(df2['rola'], categories=CLASSES3, ordered=True)
                df2 = df2.sort_values(by='rola')
                st.table(df2.style.set_table_styles([{
                    'selector': 'table',
                    'props': [
                        ('font-size', '25px')
                    ]
                }]))
        else:
            st.write('Wprowadź nazwy, aby utworzyć DataFrame.')

if __name__ == "__main__":
    main()

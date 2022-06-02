import streamlit as st
import pandas as pd
import numpy as np

st.title("Menghitung Luas Bangun Datar")
original_list=(" ", "Segitiga", "Persegi", "Persegi Panjang")
#1. as sidebar menu
add_selectbox = st.sidebar.selectbox(
    "Pilih",
    ("Segitiga", "Persegi", "Persegi Panjang", "Lingkaran", "Trapesium")
)
if add_selectbox== "Segitiga":
    st.header("Menghitung Luas Segitiga")
    a=st.number_input("Masukan Nilai Alas(cm)", 0)
    t=st.number_input("Masukan Nilai Tinggi(cm)", 0)
    hasil3=st.button("Menghitung Luas")
    if hasil3:
        Luas3 = 0.5 * a * t
        st.success(f"luasnya adalah {Luas3} cm^2")
        st.write("(0.5 x (a) x (t))")


if add_selectbox== "Persegi":
    st.header("Menghitung Luas Persegi")
    s=st.number_input("Masukan Nilai Sisi(cm)", 0)
    hasil4=st.button("Menghitung Luas")
    if hasil4:
        Luas4 = s*s
        st.success(f"luasnya adalah {Luas4}")
    
if add_selectbox== "Persegi Panjang":
    st.header("Menghitung Luas Persegi Panjang")
    p=st.number_input("Masukan Nilai Panjang(cm)", 0)
    l=st.number_input("Masukan Nilai Lebar(cm)", 0)
    hasil4a=st.button("Menghitung Luas")
    if hasil4a:
        Luas4a = p*l
        st.success(f"luasnya adalah {Luas4a}")

if add_selectbox== "Lingkaran":
    st.header("Menghitung Luas Lingkaran")
    r=st.number_input("Masukan Nilai Jari-jari (cm)", 0)
    hasilo=st.button("Menghitung Luas")
    if hasilo:
        Luaso = 3.1416 * r * r
        st.success(f"luasnya adalah {Luaso}")
    
if add_selectbox== "Trapesium":
    st.header("Menghitung Luas Trapesium")
    d1=st.number_input("Masukan Nilai Diagonal 1(cm)", 0)
    d2=st.number_input("Masukan Nilai Diagonal 2(cm)", 0)
    hasilt=st.button("Menghitung Luas")
    if hasilt:
        Luast = 0.5 * a * t
        st.success(f"luasnya adalah {Luast}")
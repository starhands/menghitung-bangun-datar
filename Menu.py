import streamlit as st
import pandas as pd
import numpy as np

st.title("Menghitung Luas Bangun Datar")
original_list=(" ", "Segitiga", "Persegi", "Persegi Panjang")
#1. as sidebar menu
add_selectbox = st.sidebar.selectbox(
    "Pilih",
    (" ", "Segitiga", "Persegi", "Persegi Panjang", "Lingkaran", "Trapesium", "Jajar Genjang", "Belah Ketupat", "Layang-Layang")
)


if add_selectbox== "Segitiga":
    st.header("Menghitung Luas Segitiga")
    a=st.number_input("Masukan Nilai Alas(cm)", 0)
    t=st.number_input("Masukan Nilai Tinggi(cm)", 0)
    hasil3=st.button("Menghitung Luas")
    if hasil3:
        Luas3 = 0.5 * a * t
        st.success(f"luasnya adalah {Luas3} cm^2")


if add_selectbox== "Persegi":
    st.header("Menghitung Luas Persegi")
    s=st.number_input("Masukan Nilai Sisi(cm)", 0)
    hasil4=st.button("Menghitung Luas")
    if hasil4:
        Luas4 = s*s
        st.success(f"luasnya adalah {Luas4} cm^2")
    
if add_selectbox== "Persegi Panjang":
    st.header("Menghitung Luas Persegi Panjang")
    p=st.number_input("Masukan Nilai Panjang(cm)", 0)
    l=st.number_input("Masukan Nilai Lebar(cm)", 0)
    hasil4a=st.button("Menghitung Luas")
    if hasil4a:
        Luas4a = p*l
        st.success(f"luasnya adalah {Luas4a} cm^2")

if add_selectbox== "Lingkaran":
    st.header("Menghitung Luas Lingkaran")
    r=st.number_input("Masukan Nilai Jari-jari (cm)", 0)
    hasilo=st.button("Menghitung Luas")
    if hasilo:
        Luaso = 3.1416 * r * r
        st.success(f"luasnya adalah {Luaso} cm^2")
    
if add_selectbox== "Trapesium":
    st.header("Menghitung Luas Trapesium")
    at=st.number_input("Masukan Nilai Sisi Atas(cm)", 0)
    al=st.number_input("Masukan Nilai Alas(cm)", 0)
    t1=st.number_input("Masukan Nilai Tinggi(cm)", 0)
    hasilt=st.button("Menghitung Luas")
    if hasilt:
        Luast = 0.5 * (at + al) * t1
        st.success(f"luasnya adalah {Luast} cm^2")
        
if add_selectbox== "Jajar Genjang":
    st.header("Menghitung Luas Jajar Genjang")
    a1=st.number_input("Masukan Nilai Panjang(cm)", 0)
    t2=st.number_input("Masukan Nilai Tinggi(cm)", 0)
    hasil5=st.button("Menghitung Luas")
    if hasil5:
        Luas5 = a1*t2
        st.success(f"luasnya adalah {Luas5} cm^2")       
        
if add_selectbox== "Belah Ketupat":
    st.header("Menghitung Luas Belah Ketupat")
    d1=st.number_input("Masukan Nilai Diagonal 1(cm)", 0)
    d2=st.number_input("Masukan Nilai Diagonal 2(cm)", 0)
    hasil6=st.button("Menghitung Luas")
    if hasil6:
        Luas6 = 0.5 * d1 * d2
        st.success(f"luasnya adalah {Luas6} cm^2")      
        
if add_selectbox== "Layang-Layang":
    st.header("Menghitung Luas Layang-Layang")
    d3=st.number_input("Masukan Nilai Diagonal 1(cm)", 0)
    d4=st.number_input("Masukan Nilai Diagonal 2(cm)", 0)
    hasil5=st.button("Menghitung Luas")
    if hasil5:
        Luas5 = 0.5 *d3 * d4
        st.success(f"luasnya adalah {Luas5} cm^2")               

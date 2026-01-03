import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Calculator", layout="centered")

html_code = """
<style>
.calc {
  width: 330px;
  margin: auto;
  background: #f5f5f5;
  padding: 16px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}
.calc-title {
  text-align: center;
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 10px;
}
.display {
  width: 100%;
  height: 65px;
  font-size: 32px;
  text-align: right;
  padding: 10px;
  margin-bottom: 14px;
  border-radius: 10px;
  border: none;
  background: #fffbe9;
}
.grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
button {
  height: 58px;
  font-size: 20px;
  font-weight: bold;
  border-radius: 10px;
  border: none;
  cursor: pointer;
}
.num { background: white; }
.op  { background: #f0f0f0; }
.eq  { background: #006064; color: white; }
.ctrl{ background: #e0e0e0; }
</style>

<div class="calc">
  <div class="calc-title">🧮 My Calculator</div>

  <input class="display" id="disp" value="0" readonly>

  <div class="grid">
    <!-- Row 1 -->
    <button class="ctrl" onclick="clr()">C</button>
    <button class="ctrl" onclick="back()">⌫</button>
    <button class="ctrl" onclick="p('%')">%</button>
    <button class="op" onclick="p('/')">÷</button>

    <!-- Row 2 -->
    <button class="num" onclick="p('7')">7</button>
    <button class="num" onclick="p('8')">8</button>
    <button class="num" onclick="p('9')">9</button>
    <button class="op" onclick="p('*')">×</button>

    <!-- Row 3 -->
    <button class="num" onclick="p('4')">4</button>
    <button class="num" onclick="p('5')">5</button>
    <button class="num" onclick="p('6')">6</button>
    <button class="op" onclick="p('-')">−</button>

    <!-- Row 4 -->
    <button class="num" onclick="p('1')">1</button>
    <button class="num" onclick="p('2')">2</button>
    <button class="num" onclick="p('3')">3</button>
    <button class="op" onclick="p('+')">+</button>

    <!-- Row 5 -->
    <button class="num" onclick="p('±')">±</button>
    <button class="num" onclick="p('0')">0</button>
    <button class="num" onclick="p('.')">.</button>
    <button class="eq" onclick="calc()">=</button>
  </div>
</div>

<script>
function p(v){
  let d = document.getElementById("disp");
  if(d.value === "0") d.value = "";
  d.value += v;
}
function clr(){
  document.getElementById("disp").value = "0";
}
function back(){
  let d = document.getElementById("disp");
  d.value = d.value.slice(0, -1) || "0";
}
function calc(){
  try{
    let exp = document.getElementById("disp").value
      .replace("×","*")
      .replace("÷","/")
      .replace("±","-");
    document.getElementById("disp").value = eval(exp);
  }catch{
    document.getElementById("disp").value = "Error";
  }
}
</script>
"""

components.html(html_code, height=600)

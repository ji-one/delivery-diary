<template>
  <div>
    <h1 class="title-logo">
      <center>
        <!--<a href="/" class="logo"
          ><img alt="Delivery Diary logo" src="../assets/test2.jpg" width="500"
        /></a>-->
        <span class="logotext"><strong>Delivery Diary</strong></span>
      </center>
    </h1>
    <h2 class="diarywrite">WRITE ON YOUR LIFESTYLE & STORY</h2>
   <div id="circle-wrapper">
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
    <div class="circle"></div>
  </div>
    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <tr>
            <th aria-label="제목"></th>
            <td>
              <input
                type="text"
                v-model="title"
                ref="subject"
                placeholder="제목을 입력하세요"
              />
              <col width="1000" />
            </td>
          </tr>
          <tr>
            <th aria-label="날씨"></th>
            <div class="form-check form-group">
              <input
                v-model.number="weather"
                class="form-check-input"
                type="radio"
                :value="1"
                id="맑음"
              />
              <div class="radio__radio"></div>
              <label class="form-check-label" for="맑음">
                <img src="../assets/sun_weather_icon.png" alt="weather-sunny" />
              </label>
              <input
                v-model.number="weather"
                class="form-check-input"
                type="radio"
                :value="2"
                id="흐림"
              />
              <div class="radio__radio"></div>
              <label class="form-check-label" for="흐림">
                <img
                  src="../assets/cloudy_weather_icon.png"
                  alt="weather-cloudy"
                />
              </label>
              <input
                v-model.number="weather"
                class="form-check-input"
                type="radio"
                :value="3"
                id="비"
              />
              <div class="radio__radio"></div>
              <label class="form-check-label" for="비">
                <img
                  src="../assets/rain_weather_icon.png"
                  alt="weather-rainy"
                />
              </label>
              <input
                v-model.number="weather"
                class="form-check-input"
                type="radio"
                :value="4"
                id="눈"
              />
              <div class="radio__radio"></div>
              <label class="form-check-label" for="눈">
                <img
                  src="../assets/snowy_weather_icon.png"
                  alt="weather-snowy"
                />
              </label>
            </div>
          </tr>
          <tr>
            <th aria-label="내용"></th>
            <td>
              <textarea
                v-model="content"
                placeholder="오늘의 이야기를 시작하세요"
              ></textarea>
            </td>
          </tr>
        </table>
      </form>
    </div>
    <div class="btnWrap">
      <button @click="fnAddProc" class="btnAdd_btn">등록</button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    //변수 생성
    return {
      title: "",
      content:"",
      weather:"",
    };
  },
  methods: {
    checkStatus(){
      if(!this.$store.state.login){
        alert("로그인이 필요한 서비스입니다.")
        this.$router.push({ path: "./signin" });
      }
    },
    fnList() {
      //리스트 화면으로 이동 함수
      this.$router.push({ path: "./list", query: this.body });
    },
    fnAddProc() {
      //등록 프로세스
      if (!this.title) {
        //제목이 없다면 값을 입력하라고 알려준다.
        alert("제목을 입력해 주세요");
        this.$refs.subject.focus(); //방식으로 선택자를 찾는다.
        return;
      }

      this.form = {
        //backend로 전송될 POST 데이터
        title: this.title,
        content: this.content,
        weather: this.weather,
      };

      this.axios
        .post("api/", this.form)
        .then((res) => {
           alert(res.data.message)
        })
        .catch((err) => {
          console.log(err);
        });
         },
  },
};
</script>

<style scoped>
.title-logo { padding: 50px 0;}
.logotext { 
  font-family: "IBM Plex Sans KR", sans-serif !important;
  font-weight: 700;
  font-size: 56px;
  color: #fff;
  transition: all .5s;
  text-shadow: 1px 2px 0 rgb(32, 95, 177);
}
.logotext:hover {
   text-shadow: 1px 2px 0 rgb(97, 138, 209),
                2px 4px 0 rgb(97, 138, 209),
                3px 6px 0 rgb(97, 138, 209),
                4px 8px 0 rgb(97, 138, 209),
                5px 10px 0 rgb(97, 138, 209),
                6px 12px 0 rgb(97, 138, 209),
              
                6px 12px 3px rgb(97, 138, 209);
}
.diarywrite {
  text-align: center;
  padding-bottom: 20px;
}
.diarywrite {
  font-family: "IBM Plex Sans KR", sans-serif !important;
  /*font-family: 'Raleway', sans-serif */
  font-weight: 300;}

/*.tbAdd{border-top:1px solid #888;}<<이 부분은 단순히 탑이 아니라 둘러싸는 걸로 만들었으면 한다.*/
/*.tbAdd th, .tbAdd td {
		border-bottom:1px solid #eee; padding:5px 0; 
		
	}*/
.AddWrap {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 100px;
}
.tbAdd {
  position: relative;
  background-color:/* #E3E6FF;*/ white;
  flex-direction: column;
  align-items: center;
  /*border: 1px solid rgb(230, 226, 226);*/
  border-radius: 5px;
 /* box-shadow: 0 0 20px rgba(0,0,0,0.15);*/
  z-index: 10;
  
}
.tbAdd th {
  content: "";
}
.tbAdd td {
  padding: 10px 10px;
  box-sizing: border-box;
}
.tbAdd td input {
  font-family: 'Lato', sans-serif !important;
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 20px;
  width: 100%;
  min-height: 50px;
  box-sizing: border-box;
  padding: 0 10px;
  border: none;
  outline: none;
  resize: none;
  color: rgb(77, 80, 94);
  background-color: rgba(68,114,196,0.2);
  border-radius: 30px;
  text-align: center;
}
.tbAdd td input::placeholder {
  text-align: center;
}

.form-check.form-group {
  display: block;
  float: right;
}

.form-check-input {
  display: none;
  padding: 20px 20px;
  margin: 0.5rem;
}
.radio__radio {
  display: inline-block;
  width: 1.25em;
  height: 1.25em;
  border: 2px solid #d8e4e2;
  border-radius: 50%;
  /*margin-right: 10px;*/
  box-sizing: border-box;
  padding: 2px;
}
.radio__radio::after {
  content: "";
  width: 100%;
  height: 100%;
  display: block;
  background-color: dodgerblue;
  border-radius: 50%;

  transform: scale(0);
  transition: transform 0.15s;
}

.form-check-input:checked + .radio__radio::after {
  transform: scale(1);
}

.form-check-label {
  display: inline-block;
  padding: 20px;
}
.form-check-label img {
  width: 30px;
  height: 30px;
}

.tbAdd td textarea {
  width: 100%;
  min-height: 300px;
  padding: 10px;
  box-sizing: border-box;
  border: none;
  outline: none;
  resize: none;
}
.tbAdd td textarea::placeholder {
  text-align: center;
}

.btnWrap {
  text-align: center;
  margin: 40px 0;
}
.btnWrap a {
  margin: 20 10px;
  text-align: center;
}
.btnAdd {
  background: #43b984;
}
.btnDelete {
  background: #f00;
}
.btn {
  
  position: relative;
  color: black;
  text-decoration: none;
  border: 1px solid #d9d6e2;
  padding: 10px 15;
  border-radius: 6px;
  margin-right: 30px;
  transition-property: background-color;
  transition-duration: 1s;
}
.btn:hover {
  background-color: #d9d6e2;
}
.btn:active {
  transition-property: background-color;
  transition-duration: 1s;
  background-color: #a3a1a7;
}

.btnadd_btn {
  position: relative;
  color: black;
  text-decoration: none;
  border: 1px solid #2381f5;
  padding: 10px 50px;
  border-radius: 6px;
  font-size: 17px;
  transition-property: background-color;
  transition-duration: 1s;
}

.btnadd_btn:hover {
  background-color: #2381f5;
}
.btnadd_btn:active {
  transition-property: background-color;
  transition-duration: 1s;
  background-color: #0877ff;
}

#circle-wrapper { 
  position: relative;

}

.circle {
  width: 246px;
  height: 246px;
  border-radius: 50%;
  
  
}
.circle:nth-child(1) {
 position: absolute;
 background-color: transparent;
 border: 1px solid rgba(0, 0, 0, 0.5);
 left: 100px;
 top: 100px;
}
.circle:nth-child(2) {
  position: absolute;
  background-color: #ffc000;
  left: 10px;
  top: 10px;
}
.circle:nth-child(3) {
  position: absolute;
  background-color: rgba(68,114,196,0.7);
  bottom: 100px;
  left: -100px;
}
.circle:nth-child(4) {
 position: absolute;
 background-color: transparent;
 border: 1px solid rgba(0, 0, 0, 0.5);
 right: 100px;
 top: 100px;
}
.circle:nth-child(5) {
  position: absolute;
  background-color: #ffc000;
  bottom: -40px;
  right: 30px;
}
.circle:nth-child(6) {
  position: absolute;
  background-color: rgba(68,114,196,0.7);
  bottom: 100px;
  right: -100px;
}
.circle:nth-child(7) {
  position: absolute;
  background-color: transparent;
  border: 1px solid rgba(68,114,196,0.7);
  top: 400px;
  left: -100px;
}
.circle:nth-child(8) {
  position: absolute;
  background-color: rgba(68,114,196,1);
  top: 500px;
  right: -100px;
}

/*Media Query-반응형 웹*/
@media screen and (max-width: 1000px){

}
/*반응형 웹 <=665*/
@media screen and (max-width: 665px){
}
  

</style>
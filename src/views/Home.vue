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
    <h2 class="diarywrite">Write on your Lifestyle & Story</h2>
    <div class="etc">
      <img class="image1" src="../assets/sky.jpg" alt="skypicture" />
      <img class="image2" src="../assets/image.png" alt="etcimage" />
      <img class="image3" src="../assets/fallen_angels.jpg" alt="steal_movie" />
      <img class="image4" src="../assets/dark_sky.jpg" alt="dark_sky" />
      <img class="image5" src="../assets/lola.jpg" alt="steal_movie2" />
      <img class="image6" src="../assets/night.jpg" alt="night" />
      <img class="tape1" src="../assets/papertape.png" alt="papertape" />
      <img class="tape2" src="../assets/papertape2.png" alt="papertape2" />
      <img class="flower" src="../assets/flower.png" alt="flower" />
      <div class="rectangle"></div>
      <div class="small_re"></div>
      <div class="small_re2"></div>
      <div class="small_re3"></div>
      <div class="small_re4"></div>
      <div class="small_re5"></div>
    </div>

    <div class="AddWrap">
      <form>
        <table class="tbAdd">
          <!--<colgroup>
                    <col width="200"/>
                 </colgroup>-->
          <tr>
            <th aria-label="제목"></th>
            <td>
              <input
                type="text"
                v-model="subject"
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
                v-model.number="typeOfTask"
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
                v-model.number="typeOfTask"
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
                v-model.number="typeOfTask"
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
                v-model.number="typeOfTask"
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
                v-model="cont"
                ref="cont"
                placeholder="오늘의 이야기를 시작하세요"
              ></textarea>
            </td>
          </tr>
        </table>
      </form>
    </div>

    <div class="btnWrap">
      <!--<a href="javascripit:;" @click="fnList" class="btn">임시목록</a>-->
      <a href="javascripit:;" @click="fnAddProc" class="btnAdd_btn">등록</a>
    </div>
  </div>
</template>



<script>
export default {
  data() {
    //변수 생성
    return {
      board_code: "news",
      subject: "",
      cont: "",
      id: "admin",
      //,form:'' //form 전송 데이터
      typeOfTask: null,
    };
  },
  methods: {
    fnList() {
      //리스트 화면으로 이동 함수
      this.$router.push({ path: "./list", query: this.body });
    },
    fnAddProc() {
      //등록 프로세스
      if (!this.subject) {
        //제목이 없다면 값을 입력하라고 알려준다.
        alert("제목을 입력해 주세요");
        this.$refs.subject.focus(); //방식으로 선택자를 찾는다.
        return;
      }

      this.form = {
        //backend로 전송될 POST 데이터
        board_code: this.board_code,
        subject: this.subject,
        cont: this.cont,
        id: this.id,
      };

      this.$axios
        .post("http://localhost:3000/api/delivery-diary", this.form)
        .then((res) => {
          if (res.data.success) {
            alert("등록되었습니다.");
            this.fnList();
          } else {
            alert("실행중 실패했습니다.\n다시 이용해 주세요");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
/*반응형 웹

반응 기준

로고 관련 앵커가 너무 아래에 배치되어있음. 변환필요.<ok>

페이지 색 정해보기

입력창은 고정 값이 있는 것 같긴하다.
사진은 오히려 뒤에서 좌우 값에 따라 움직이네
이걸 없앨지를 정해야함
오른쪽은 right0이라서 벽에 붙어있고
왼쪽이 바뀐디

입력창의 사이즈/입력창 좌우 패딩값(은있고)
최소 고정값을 정해놓으면 될듯<ok>

사진 없애는 것

글자수 입력하는 값 뜨도록 넣기///

사진 가로 정열할지말지.*/

/*.logo img { 
            margin-top: 50px;
            
            }*/

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
   text-shadow: 1px 2px 0 rgb(32, 95, 177),
                2px 4px 0 rgb(32, 95, 177),
                3px 6px 0 rgb(32, 95, 177),
                4px 8px 0 rgb(32, 95, 177),
                5px 10px 0 rgb(32, 95, 177),
                6px 12px 0 rgb(32, 95, 177),
              
                6px 12px 3px rgba(32, 95, 177,0.8);
}
.diarywrite {
  text-align: center;
  padding-bottom: 20px;
}
.diarywrite {
  font-family: "IBM Plex Sans KR", sans-serif !important;
  
  font-weight: 300;
}
.tape1,
  .tape2,
  .flower{
    display: none;
    position: absolute;
  }
.image1 {
  position: absolute;
  border-radius: 5px;
  border: 1px solid whitesmoke;
  border-width: 20px 10px 70px 10px;
  bottom: 500px;
  right: 50px;
  width: 200px;
  height: 350px;
  z-index: 2;
  transition: transform 1.3s;
}
.image1:hover {
  transform: scale(1.05);
  transition: transform 1.3s;
}

.image2 {
  position: absolute;
  border-radius: 4px;
  bottom: 200px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}
.image3 {
  position: absolute;
  border-radius: 4px;
  bottom: 420px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 8;
  transition: transform 1s;
}
.image4 {
  position: absolute;
  border-radius: 4px;
  bottom: -20px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image5 {
  position: absolute;
  border-radius: 4px;
  bottom: 640px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image6 {
  position: absolute;
  border-radius: 4px;
  bottom: 860px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image2:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image3:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image4:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image5:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image6:hover {
  transform: scale(1.03);
  transition: transform 1s;
}

.rectangle {
  position: absolute;
  border-radius: 5px;
  bottom: 480px;
  right: -10;
  width: 280px;
  height: 390px;
  background-color: rgba(30, 143, 255, 0.37);
  z-index: 1;
}
.small_re {
  position: absolute;
  background-color: rgb(157, 148, 180);
  width: 200px;
  height: 1500px;
  bottom: -30px;
  left: 56px;
  z-index: 3;
}
.small_re2 {
  position: absolute;
  background-color: rgb(255, 255, 255);
  width: 120px;
  height: 20px;
  bottom: 250px;
  left: 70px;
  z-index: 6;
}
.small_re3 {
  position: absolute;
  background-color: rgb(81, 190, 253);
  width: 100px;
  height: 20px;
  bottom: 150px;
  left: 180px;
  z-index: 7;
}
.small_re4 {
  position: absolute;
  background-color: white;
  width: 90px;
  height: 20px;
  left: 70px;
  bottom: 700px;
  z-index: 8;
}
.small_re5 {
  position: absolute;
  background-color: rgb(81, 190, 253);
  width: 120px;
  height: 20px;
  left: 160px;
  bottom: 450px;
  z-index: 8;
}


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
  background-color: white;
  flex-direction: column;
  align-items: center;
  /*border: 1px solid rgb(230, 226, 226);*/
  border-radius: 5px;
  box-shadow: 0 0 20px rgba(0,0,0,0.15);
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
  font-family: "IBM Plex Sans KR", sans-serif !important;
  font-weight: 700;
  font-size: 20px;
  width: 100%;
  min-height: 30px;
  box-sizing: border-box;
  padding: 0 10px;
  border: none;
  outline: none;
  resize: none;
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
  width: 50px;
  height: 50px;
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

/*Media Query-반응형 웹*/
@media screen and (max-width: 1000px){

  .tape1,
  .tape2,
  .flower{
    display: block;
    position: absolute;
  }
  .tape1 {
    width: 200px;
    height: 50px;
    bottom: 700px;
    right: 50px;
    -webkit-animation: shake .4s ease-in-out .4s infinite alternate;
  }
  .tape2 {
    width: 200px;
    height: 50px;
    bottom: 680px;
    right: 35px;
    -webkit-animation: shake2 .5s ease-in-out .5s infinite alternate;
  }
  .flower {
    bottom: 605px;
    width: 180px;
    height: 90px;
    left: 60px;
  }

  @-webkit-keyframes shake {
    from { -webkit-transform: rotate(0deg);}
    to { -webkit-transform: rotate(-2deg);
        -webkit-transform-origin: center center;}
  }
  @-webkit-keyframes shake2 {
    from { -webkit-transform: rotate(0deg);}
    to { -webkit-transform: rotate(-1deg);
        -webkit-transform-origin: center center;}
  }
  
  .image1 {
  display:none;
  position: absolute;
  border-radius: 5px;
  border: 1px solid whitesmoke;
  border-width: 20px 10px 70px 10px;
  bottom: 500px;
  right: 50px;
  width: 200px;
  height: 350px;
  z-index: 2;
  transition: transform 1.3s;
}
.image1:hover {
  transform: scale(1.05);
  transition: transform 1.3s;
}

.image2 {
  display:none;
  position: absolute;
  border-radius: 4px;
  bottom: 200px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}
.image3 {
  display:none;
  position: absolute;
  border-radius: 4px;
  bottom: 420px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 8;
  transition: transform 1s;
}
.image4 {
  display:none;
  position: absolute;
  border-radius: 4px;
  bottom: -20px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image5 {
  display:none;
  position: absolute;
  border-radius: 4px;
  bottom: 640px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image6 {
  display:none;
  position: absolute;
  border-radius: 4px;
  bottom: 860px;
  left: 80px;
  width: 150px;
  height: 200px;
  z-index: 4;
  transition: transform 1s;
}

.image2:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image3:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image4:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image5:hover {
  transform: scale(1.03);
  transition: transform 1s;
}
.image6:hover {
  transform: scale(1.03);
  transition: transform 1s;
}

.rectangle {
  display:none;
  position: absolute;
  border-radius: 5px;
  bottom: 480px;
  right: -10;
  width: 280px;
  height: 390px;
  background-color: rgba(30, 143, 255, 0.37);
  z-index: 1;
}
.small_re {
  display:none;
  position: absolute;
  background-color: rgb(157, 148, 180);
  width: 200px;
  height: 1500px;
  bottom: -30px;
  left: 56px;
  z-index: 3;
}
.small_re2 {
  display:none;
  position: absolute;
  background-color: rgb(255, 255, 255);
  width: 120px;
  height: 20px;
  bottom: 250px;
  left: 70px;
  z-index: 6;
}
.small_re3 {
  display:none;
  position: absolute;
  background-color: rgb(81, 190, 253);
  width: 100px;
  height: 20px;
  bottom: 150px;
  left: 180px;
  z-index: 7;
}
.small_re4 {
  display:none;
  position: absolute;
  background-color: white;
  width: 90px;
  height: 20px;
  left: 70px;
  bottom: 700px;
  z-index: 8;
}
.small_re5 {
  display:none;
  position: absolute;
  background-color: rgb(81, 190, 253);
  width: 120px;
  height: 20px;
  left: 160px;
  bottom: 450px;
  z-index: 8;
}

}

</style>
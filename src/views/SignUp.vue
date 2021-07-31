<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">이름: </label>
      <input type="text" id="username" v-model="credentials.username" />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" />
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input
        type="password"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
      />
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
        passwordConfirmation: "",
      },
    };
  },
  methods: {
    signup: function() {
      axios({
        method: "post",
        url: "http://localhost:8000/common/signup/",
        data: this.credentials,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">이름: </label>
      <input type="text" id="username" v-model="credentials.username" />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" />
    </div>

    <button @click="login">회원가입</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignIn",
  data: function() {
    return {
      credentials: {
        username: null,
        password: null,
      },
    };
  },
  methods: {
    login: function () {
      axios({
        method: "post",
        url: "http://localhost:8000/common/api-token-auth/",
        data: this.credentials,
      })
        .then((res) => {
          localStorage.setItem("jwt", res.data.token);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

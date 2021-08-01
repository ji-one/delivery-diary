<template>
  <v-card>
    <v-card-title>
      <v-img
        src="https://i.ibb.co/QdR6XMt/Kakao-Talk-Photo-2021-08-01-23-59-37.jpg"
      ></v-img>
    </v-card-title>
    <v-card-text>
      <v-form v-model="valid">
        <v-text-field
          label="아이디"
          v-model="credentials.username"
          prepend-icon="mdi-account-circle"
          :rules="[(v) => !!v || '아이디를 입력해주세요.']"
          required
        >
        </v-text-field>
        <v-text-field
          label="비밀번호"
          v-model="credentials.password"
          prepend-icon="mdi-lock-outline"
          type="password"
          :rules="[(v) => !!v || '비밀번호를 입력해주세요.']"
          required
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-end">
      <v-btn @click="signin" rounded text color="primary">로그인</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "SignIn",
  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
        passwordConfirmation: "",
      },
      token: "",
      decoded: "",
    };
  },
  methods: {
    signin() {
      const jwt = require("jsonwebtoken");
      this.axios
        .post("http://localhost:8000/common/api-token-auth/", this.credentials)
        .then((res) => {
          this.token = res.data.token;
          sessionStorage.token = this.token;
          this.decoded = jwt.decode(sessionStorage.token);
          this.$store.commit("get_token", this.decoded);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};
</script>

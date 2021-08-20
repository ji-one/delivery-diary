<template>
  <v-card>
    <v-card-title>
      로그인
    </v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="아이디"
          v-model="credentials.username"
          :rules="[(v) => !!v || '아이디를 입력해주세요.']"
          required
        >
        </v-text-field>
        <v-text-field
          label="비밀번호"
          v-model="credentials.password"
          :rules="[(v) => !!v || '비밀번호를 입력해주세요.']"
          :type="isPasswordHide ? 'password' : 'text'"
          :append-icon="isPasswordHide ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append="isPasswordHide = !isPasswordHide"
          required
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-space-between">
      <v-btn to="/signup" rounded text>회원이 아니신가요?</v-btn>
      <v-btn :disabled="!isValid" @click="signin" rounded text color="primary"
        >로그인</v-btn
      >
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
      isPasswordHide: true,
      isValid: false,
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
          alert(err.response.data.error);
        });
    },
  },
};
</script>

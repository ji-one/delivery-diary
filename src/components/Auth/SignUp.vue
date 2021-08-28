<template>
  <v-card>
    <v-card-title>계정 만들기</v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="아이디*"
          v-model="credentials.username"
          :rules="[(v) => !!v || '아이디는 필수 입력사항입니다.']"
          required
        >
        </v-text-field>
        <v-text-field
          label="비밀번호*"
          v-model="credentials.password"
          :rules="[(v) => !!v || '비밀번호는 필수 입력사항입니다.']"
          :type="isPasswordHide ? 'password' : 'text'"
          :append-icon="isPasswordHide ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append="isPasswordHide = !isPasswordHide"
          required
        >
        </v-text-field>
        <v-text-field
          label="비밀번호 확인*"
          v-model="credentials.passwordConfirmation"
          type="password"
          :rules="[
            (v) => !!v || '비밀번호 확인은 필수 입력사항입니다.',
            (v) =>
              v === credentials.password || '비밀번호가 일치하지 않습니다.',
          ]"
          required
        >
        </v-text-field>
        <v-text-field
          label="닉네임*"
          v-model="credentials.nickname"
          :rules="[(v) => !!v || '닉네임은 필수 입력사항입니다.']"
          required
        >
        </v-text-field>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          :return-value.sync="date"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="credentials.birthday"
              label="생일"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker v-model="credentials.birthday" no-title scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="menu = false">
              Cancel
            </v-btn>
            <v-btn text color="primary" @click="$refs.menu.save(date)">
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
        <v-text-field
          label="전화번호*"
          v-model="credentials.phone_number"
          :rules="[
            (v) => !!v || '전화번호는 필수 입력사항입니다.',
            (v) => /^[0-9]+$/g.test(v) || '숫자만 입력해주세요.',
          ]"
          placeholder="하이픈(-)을 제외하고 숫자만 입력해 주세요."
          required
        >
        </v-text-field>
        <v-text-field
          label="주소*"
          v-model="credentials.address"
          :rules="[(v) => !!v || '주소는 필수 입력사항입니다.']"
          placeholder="일기 수령이 가능한 주소로 입력해주세요."
          required
        >
        </v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-space-between">
      <v-btn to="/signin" rounded text>이미 계정이 있으신가요?</v-btn>
      <v-btn :disabled="!isValid" @click="signup" rounded text color="primary"
        >계정 생성</v-btn
      >
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: "SignUp",
  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
        passwordConfirmation: "",
        nickname: "",
        birthday: "",
        phone_number: "",
        address: "",
      },
      isPasswordHide: true,
      isValid: false,
    };
  },
  methods: {
    signup() {
      this.axios
        .post("common/signup/", this.credentials)
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          alert(err.response.data.error);
        });
    },
  },
};
</script>

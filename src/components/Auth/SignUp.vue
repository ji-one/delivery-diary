<template>
  <v-card>
    <v-card-title
      ><v-img
        src="https://i.ibb.co/QdR6XMt/Kakao-Talk-Photo-2021-08-01-23-59-37.jpg"
      ></v-img
    ></v-card-title>
    <v-card-text>
      <v-text-field
        label="아이디*"
        v-model="credentials.username"
        prepend-icon="mdi-account-circle"
        :rules="[(v) => !!v || '아이디는 필수 입력사항입니다.']"
        required
      >
      </v-text-field>
      <v-text-field
        label="비밀번호*"
        v-model="credentials.password"
        prepend-icon="mdi-lock-outline"
        type="password"
        :rules="[(v) => !!v || '비밀번호는 필수 입력사항입니다.']"
        required
      >
      </v-text-field>
      <v-text-field
        label="비밀번호 확인*"
        v-model="credentials.passwordConfirmation"
        prepend-icon="mdi-lock"
        type="password"
        :rules="[
          (v) => !!v || '비밀번호 확인은 필수 입력사항입니다.',
          (v) => v === credentials.password || '비밀번호가 일치하지 않습니다.',
        ]"
        required
      >
      </v-text-field>
      <v-text-field
        label="닉네임*"
        v-model="credentials.nickname"
        prepend-icon="mdi-owl"
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
            prepend-icon="mdi-calendar"
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
        prepend-icon="mdi-cellphone-android"
        :rules="[(v) => !!v || '전화번호는 필수 입력사항입니다.']"
        required
      >
      </v-text-field>
      <v-text-field
        label="주소*"
        v-model="credentials.address"
        prepend-icon="mdi-home-outline"
        :rules="[(v) => !!v || '주소는 필수 입력사항입니다.']"
        required
      >
      </v-text-field>
      <v-card-actions class="justify-end">
        <v-btn @click="signup" rounded text color="primary">회원가입</v-btn>
      </v-card-actions>
    </v-card-text>
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
    };
  },
  methods: {
    signup() {
      this.axios
        .post("http://localhost:8000/common/signup/", this.credentials)
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          alert(err);
        });
    },
  },
};
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="5">
        <v-card>
          <v-card-title>마이페이지</v-card-title>
          <v-card-text>
            <v-form v-model="isValid">
              <v-text-field
                label="아이디"
                v-model="userInfo.username"
                prepend-icon="mdi-account-circle"
                readonly
              >
              </v-text-field>
              <v-text-field
                label="닉네임"
                v-model="userInfo.nickname"
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
                    v-model="userInfo.birthday"
                    label="생일"
                    prepend-icon="mdi-calendar"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                  ></v-text-field>
                </template>
                <v-date-picker v-model="userInfo.birthday" no-title scrollable>
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
                label="전화번호"
                v-model="userInfo.phone_number"
                prepend-icon="mdi-cellphone-android"
                :rules="[(v) => !!v || '전화번호는 필수 입력사항입니다.']"
                required
              >
              </v-text-field>
              <v-text-field
                label="주소"
                v-model="userInfo.address"
                prepend-icon="mdi-home-outline"
                :rules="[(v) => !!v || '주소는 필수 입력사항입니다.']"
                required
              ></v-text-field>
            </v-form>
            <v-card-actions class="justify-end">
              <ChangePassword />
              <v-btn
                :disabled="!isValid"
                @click="update"
                rounded
                text
                color="primary"
                >수정</v-btn
              >
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import ChangePassword from "../components/MyPage/ChangePassword.vue";
export default {
  name: "MyPage",
  components: {
    ChangePassword,
  },
  data: function() {
    return {
      userInfo: {
        username: "",
        nickname: "",
        birthday: "",
        phone_number: "",
        address: "",
      },
      isValid: false,
    };
  },

  created() {
    this.userInfo.username = this.$store.state.username;
    this.userInfo.nickname = this.$store.state.nickname;
    this.userInfo.birthday = this.$store.state.birthday;
    this.userInfo.phone_number = this.$store.state.phone_number;
    this.userInfo.address = this.$store.state.address;
  },

  methods: {
    update() {
      const jwt = require("jsonwebtoken");
      this.axios
        .patch("http://localhost:8000/common/update/info/", this.userInfo)
        .then(() => {
          this.axios
            .post("http://localhost:8000/common/api-token-auth/refresh/", {
              username: this.userInfo.username,
            })
            .then((res) => {
              sessionStorage.token = res.data.token;
              this.$store.commit("get_token", jwt.decode(sessionStorage.token));
              alert("성공적으로 수정되었습니다.");
            });
        });
    },
    // onFileChange(event) {
    //   this.userInfo.profile_image = event.target.files[0];
    // },
  },
};
</script>

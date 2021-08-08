<template>
  <v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" rounded text v-bind="attrs" v-on="on">
          비밀번호 변경
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">비밀번호 변경</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-form v-model="isValid">
                  <v-text-field
                    label="새 비밀번호"
                    v-model="newPassword"
                    type="password"
                    :rules="[(v) => !!v || '비밀번호는 필수 입력사항입니다.']"
                    required
                  ></v-text-field>
                  <v-text-field
                    label="새 비밀번호 확인"
                    v-model="passwordConfirmation"
                    type="password"
                    :rules="[
                      (v) => !!v || '비밀번호 확인은 필수 입력사항입니다.',
                      (v) =>
                        v === newPassword || '비밀번호가 일치하지 않습니다.',
                    ]"
                    required
                  ></v-text-field>
                </v-form>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text rounded @click="dialog = false">
            취소
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            rounded
            :disabled="!isValid"
            @click="changePassword"
          >
            수정
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>
<script>
export default {
  name: "changePassword",
  data: () => ({
    newPassword: "",
    passwordConfirmation: "",
    dialog: false,
    isValid: false,
  }),
  methods: {
    changePassword() {
      const jwt = require("jsonwebtoken");
      this.axios
        .patch("http://localhost:8000/common/update/password/", {
          username: this.$store.state.username,
          newPassword: this.newPassword,
          passwordConfirmation: this.passwordConfirmation,
        })
        .then(() => {
          this.axios
            .post("http://localhost:8000/common/api-token-auth/refresh/", {
              username: this.$store.state.username,
            })
            .then((res) => {
              sessionStorage.token = res.data.token;
              this.$store.commit("get_token", jwt.decode(sessionStorage.token));
              this.dialog = false;
            });
        });
    },
  },
};
</script>

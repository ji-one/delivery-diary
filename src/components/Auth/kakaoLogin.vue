<template>
  <img
    class="kakao_btn"
    src="@/assets/kakao_login_medium_narrow.png"
    @click="login"
  />
</template>

<script>
export default {
  name: "kakaoLogin",
  methods: {
    login() {
      window.Kakao.Auth.login({
        scope: "account_email",
        success: function(authObj) {
          console.log(authObj);
          window.Kakao.API.request({
            url: "/v2/user/me",
            success: (res) => {
              const kakao_account = res.kakao_account;
              console.log(kakao_account);
            },
          });
        },
      });
    },
  },
};
</script>
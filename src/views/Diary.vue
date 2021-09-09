<template>
  <v-container fill-height justify-center>
    <v-layout justify-center>
      <v-flex mt-10>
        <div>
          <v-card>
            <v-card-title>
              My Diary
              <v-spacer></v-spacer>
              <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search"
                single-line
              ></v-text-field>
            </v-card-title>
            <v-dialog v-model="dialog" width="800">
              <v-card height="700">
                <v-card-title class="text-h5 grey lighten-2">
                  {{ this.form.title }}
                </v-card-title>
                <v-card-subtitle>{{ this.form.created_at }}</v-card-subtitle>
                <v-card-text>{{ this.form.content }}</v-card-text></v-card
              ></v-dialog
            >
            <v-data-table
              :headers="headers"
              :items="diaries"
              :search="search"
              @click:row="showDetail"
            >
              <template slot="items" slot-scope="props">
                <td :class="headers[0].class">
                  {{ props.item.title }}
                </td>
                <td :class="headers[1].class">
                  {{ props.item.created_at }}
                </td>
              </template>
            </v-data-table>
          </v-card>
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "Board",
  data: () => ({
    form: {},
    search: "",
    dialog: false,
    diaries: [],
    headers: [
      {
        text: "제목",
        value: "title",
        sortable: true,
      },
      {
        text: "작성 날짜",
        value: "created_at",
        sortable: false,
      },
    ],
  }),
  mounted() {
    this.axios
      .get("api/diary")
      .then((res) => {
        res.data.forEach((e) => {
          this.diaries.push({
            title: e.fields.title,
            created_at: (e.fields.created_at + "").substring(0, 10),
            content: e.fields.content,
            weather: e.fields.weather,
          });
          console.log(e);
        });
      })
      .catch((e) => console.log(e));
  },
  methods: {
    showDetail(data) {
      console.log(data);
      this.form = data;
      this.dialog = true;
    },
  },
};
</script>

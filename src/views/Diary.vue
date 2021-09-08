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
                hide-details
              ></v-text-field>
            </v-card-title>
            <v-data-table
              :headers="headers"
              :items="diaries"
              :search="search"
              @click:row="detail"
            >
              <template slot="items" slot-scope="props">
                <td :class="headers[0].class">{{ props.item.title }}</td>
                <td :class="headers[2].class">
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
    id: "",
    search: "",
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
          });
          console.log(e);
        });
      })
      .catch((e) => console.log(e));
  },
};
</script>

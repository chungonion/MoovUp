<template>
  <v-container class="grey lighten-5">
    <v-row>
      <v-col sm="6">
        <v-toolbar>
          <template v-slot:prepend>
            <v-btn icon @click="onClick">
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </template>
        </v-toolbar>
        <friends-detail
          :email="email"
          :lat="lat"
          :lon="lon"
          :lastName="lastName"
          :firstName="firstName"
          :id="id"
          :picture="picture"
        ></friends-detail>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
<script>
import FriendsDetail from "../components/FriendsDetail.vue";

export default {
  components: { FriendsDetail },
  props: ["id", "firstName", "lastName", "email", "picture", "lon", "lat"],
  created() {
    console.log(this.$props);
  },
  methods: {
    onClick() {
      this.$router.back();
    },
  },
};
</script>

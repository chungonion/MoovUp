<template>
  <div class="d-flex align-center flex-column mb-3" @click="onClick">
    <v-card min-width="400">
      <v-list-item class="w-100">
        <v-avatar
          color="grey-darken-3"
          v-bind:image="picture"
          size="large"
          left
        ></v-avatar>
        <v-card-title>
          <span>{{ firstName }} {{ lastName }}</span>
        </v-card-title>
      </v-list-item>
    </v-card>
  </div>
</template>

<script setup></script>
<script>
export default {
  name: "FriendsCard.vue",
  props: ["id", "firstName", "lastName", "email", "picture", "lon", "lat"],
  methods: {
    onClick() {
      let prop = {
        id: this.$props.id,
        firstName: this.$props.firstName,
        lastName: this.$props.lastName,
        email: this.$props.email,
        lon: this.$props.lon,
        lat: this.$props.lat,
        picture: this.$props.picture,
      };
      this.$router.push({ name: "friendsDetail", params: prop });
    },
  },
};
</script>

<style scoped>
@import "@coreui/coreui/dist/css/coreui.min.css";
@import "bootstrap/dist/css/bootstrap.min.css";

CCard {
  width: 18rem;
}
</style>

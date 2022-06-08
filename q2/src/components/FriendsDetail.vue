<template>
  <div class="d-flex align-start flex-column">
    <GMapMap
      :center="{ lat: Number(this.$props.lat), lng: Number(this.$props.lon) }"
      :zoom="15"
      map-type-id="terrain"
      style="width: 400px; height: 500px"
    >
      <GMapMarker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
      />
    </GMapMap>
    <br />
    <div class="row">
      <FriendsCard
        :key="id"
        :id="id"
        :first-name="firstName"
        :last-name="lastName"
        :email="email"
        :picture="picture"
      >
        <!--        <div @click="onClick">{{ item.name.first }} {{ item.name.last }}</div>-->
      </FriendsCard>
    </div>
  </div>
</template>

<script setup>
import FriendsCard from "../components/FriendsCard.vue";
</script>
<script>
export default {
  name: "FriendsDetail",
  props: ["id", "firstName", "lastName", "email", "picture", "lon", "lat"],
  data() {
    return {
      center: { lat: Number(this.$props.lat), lng: Number(this.$props.lon) },
      markers: [
        {
          position: {
            lat: Number(this.$props.lat),
            lng: Number(this.$props.lon),
          },
        },
      ],
    };
  },
  created() {
    console.log(this.$props.picture);
  },
};
</script>

<style scoped></style>

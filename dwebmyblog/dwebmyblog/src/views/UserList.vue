<template>
  <div id="userlist">
    <div v-for="item in imglist" v-bind:key="item.pk" class="user">
      <img :src="'https://api.dweb.club/'+item.pic" alt />
      <p>{{ item.title }}</p>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
export default {
  data() {
    return {
      imglist: [],
    };
  },
  //用户在看到界面之前，最后vue提供的一次函数执行
  mounted() {

  },
  methods: {
  },
};
</script>

<style>
</style>
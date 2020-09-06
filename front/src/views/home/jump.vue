<template>
  <div class="home-page">
    <h1 class="title" style="font-family: 'Blacker Text'; font-weight: bold;"> Waiting...... </h1>
    <el-button class="check" @click="clickButton" style="font-family: 'Blacker Text'; font-weight: bold; display:block;"> Check </el-button>
  </div>
</template>

<script>

export default {
  name: 'Jump',
  data() {
    return {
      info: {}
    }
  },
  watch: {

  },
  mounted() {
    this.getParams()
    // console.log(this.info)
  },
  methods: {
    getParams() {
      this.info = this.$route.query.site
    },
    clickButton: function() {
      this.$router.push({
        path: '/task/participated_task',
        query: {
          site: this.info
        }
      })
    }
  }
}
</script>

<style>
.check {
  position: absolute;
  left: 46%;
  top: 48%;
  background-color: #274c4a;
  color: white;
}
.title {
  position: absolute;
  left: 43%;
  top: 33%;
  font-size: 48px;
}
</style>

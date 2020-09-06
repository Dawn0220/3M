<template>
  <div class="employer-one bg-box" style="font-family: 'jdjszhong'; font-weight: bold; display:block;">
    <div class="name indent">
      <h1> {{ name }} </h1>
    </div>
    <div class="description indent">
      <h3> Description: </h3>
      <h3 class="one"> {{description1}} </h3>
    </div>
    <div class="address indent">
      <h3> Address: </h3>
      <h3 class="two"> {{description2}} </h3>
    </div>
    <div class="quota indent">
      <h3> Quota: </h3>
      <h3 class="three"> {{people}} </h3>
    </div>
    <div class="form indent">
      <h3> Form: </h3>
      <h3 class="four"> {{form}} </h3>
    </div>

    <div class="pic">
      <img v-if="condition1" src="../../assets/xuexiao.jpeg" class="picture bg-box" alt="picture">
    </div>
    <div class="pic">
      <img v-if="condition2" src="../../assets/jubensha.jpeg" class="picture bg-box" alt="picture">
    </div>
    <div class="pic">
      <img v-if="condition3" src="../../assets/huanle.jpeg" class="picture bg-box" alt="picture">
    </div>
    <div class="pic">
      <img v-if="condition4" src="../../assets/xicha.jpg" class="picture bg-box" alt="picture">
    </div>
    <div class="pic">
      <img v-if="condition5" src="../../assets/dianyingyuan.jpeg" class="picture bg-box" alt="picture">
    </div>

    <div class="button">
      <el-button class="sign" @click="clickButton" style="font-family: 'Blacker Text'; font-weight: bold; display:block;"> Apply </el-button>
    </div>
    <h3 class="six"> {{address}} </h3>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: 'Employer',
  data() {
    return {
      employer: {},
      name: '',
      address: '',
      people: '',
      form: '',
      web: '',
      url: '../../../public/xuexiao.jpeg',
      description1: '',
      description2: '',
      condition1: null,
      condition2: null,
      condition3: null,
      condition4: null,
      condition5: null,
    }
  },
  watch: {

  },
  mounted() {
    this.getParams()
    // console.log(this.employer)
    this.name = this.employer.name
    if (this.name === "喜茶"){
      this.address = '福田区中康路卓悦汇商场L01楼L1-36号'
      this.people = '一男一女'
      this.form = '品尝'
      this.web = '../../../public/xicha.jpg'
      this.description1 = '2012年，原名皇茶ROYALTEA。为了与层出不穷的山寨品牌区分开来，故全面升级为注册品牌喜茶HEYTEA。喜茶为芝士现泡茶的原创者。自创立以来，喜茶专注于呈现来自世界各地的优质茶香，让茶饮这一古老文化焕发出新的生命力。现在，喜茶仍是最受欢迎的饮料品牌之一。'
      this.description2 = '本店诚挚邀请一对有缘男女一同品尝当季水果限定系列中最新上线的“生打椰椰奶冻”和“生打椰椰芒”，协助我店新品能更好地适应两性口味的共同喜好。参与者将有机会获得本店的饮品特惠哦~'
    }
    this.getPic()
    this.address = this.employer.value[2]
    this.people = this.employer.value[4]
    this.form = this.employer.value[5]
    this.web = this.employer.value[6]
    this.description1 = this.employer.value[7]
    this.description2 = this.employer.value[8]
    // console.log(this.description1)
    // console.log(this.web)
  },
  methods: {
    getPic: function() {
      if (this.name === '香港中文大学（深圳）') this.condition1 = true
      if (this.name === '月石剧本杀') this.condition2 = true
      if (this.name === '欢乐时光') this.condition3 = true
      if (this.name === '喜茶') this.condition4 = true
      if (this.name === '英嘉尼私人影院') this.condition5 = true
    },
    getParams() {
      this.employer = this.$route.query.site
    },
    clickButton: function() {
      this.$router.push({
        path: '/jump/1',
        query: {
          site: this.employer
        }
      })
    },
  }
}
</script>

<style scoped>
.four {
  position: absolute;
  left: 13%;
  top: -85%;
}
.three {
  position: absolute;
  left: 13%;
  top: -80%;
}
.six {
  position: absolute;
  left: 16%;
  top: 45%;
  width: 50%;
}
.picture {
  position: absolute;
  left: 12%;
  top: 15%;
  width: 50%;
  height: 50%;
}
.sign {
  position: absolute;
  left: 45%;
  top: 92%;
}
.pic {
  position: absolute;
  width: 75%;
  height: 75%;
  left: 50%;
  top: 25;
}
.two {
  position: absolute;
  left: 13%;
  top: -700%;
  width: 80%;
}
.one {
  position: absolute;
  left: 13%;
  top: -85%;
  width: 80%;
}
.description {
  position: relative;
  top: 5%;
}
.address {
  position: relative;
  top: 30%;
}
.quota {
  position: relative;
  top: 40%;
}
.form {
  position: absolute;
  top: 50%;
}
.indent {
  position: relative;
  left: 3%;
}
.employer-one {
  position: absolute;
  width: 80%;
  height: 80%;
  left: 10%;
  top: 5%;
}
.bg-box {
  border-radius: 2%;
  border-width: 10px;
  box-shadow: 0px 0px 3px #274c4a;
  background-color: white;
  box-sizing: border-box;
  /* text-align: center; */
}
.sign{
  background-color: #274c4a;
  color: white;
}
</style>

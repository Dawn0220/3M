<template>
  <div class="temp">
    <div id="temp-chart" ref="map" class="temp-chart" />
  </div>
</template>

<script>
// 注意在 index.html 引入全局的百度地图 JS
// script src=""http://api.map.baidu.com/getscript?v=3.0&ak=Xjmh9v5jGa******6ZVf0PU2ueSedr5F"

// 引入基本模板
// let echarts = require("echarts/lib/echarts");

// 引入百度扩展
// require("echarts/extension/bmap/bmap");
import echarts from 'echarts'
import 'echarts/extension/bmap/bmap.js'
import 'echarts/extension/bmap/BMapCoordSys.js'
import 'echarts/extension/bmap/BMapModel.js'
import 'echarts/extension/bmap/BMapView.js'
// import mapConfig from '/Users/zhouzeyu/custom_map_config.json'
// import axios from 'axios'

export default {
  name: 'Temp',
  data() {
    return {
      freeData: [
        { name: '香港中文大学（深圳）', value: [114.218297, 22.692285, '龙岗区龙翔大道2001号', '广东省最好的大学之一', '一男一女', '参观', '../../../public/xuexiao.jpeg', '香港中文大学（深圳）是一所经国家教育部批准，按中外合作办学条例设立，传承香港中文大学的办学理念和学术体系的大学。以创建一所立足中国、面向世界的一流研究型大学为己任，致力于培养具有国际视野、中华传统和社会担当的创新型高层次人才。', '作为一所尚还年轻的大学，本校邀请两位同学一同参观本校环境与设施，希望二位在参观的过程中能更好地了解香港中文大学（深圳）。二位参与者将获得校内奶茶店一瓯茶的优惠券与校内任一食堂的优惠券。'] },
        { name: '月石剧本杀', value: [113.950382, 22.546199, '南山区科兴路11-1深南花园裙楼C区328', '深圳剧本杀人气排名第一', '四男四女', '体验', '../../../public/jubensha.jpeg', '本店为深圳市人气排名第一的线下沉浸式体验剧本杀，在环境优美的同时，本店还拥有丰富且剧情严谨的各类剧本，诸如今日人气爆棚的恐怖剧本《第二十二条校规》，火爆推理剧本《百日孤灯》和古风剧本《鸢飞戾天》等，此外本店还拥有最热情的主持人带领玩家更好地沉浸于剧本氛围。', '诚挚邀请四位小哥哥和四位小姐姐组队体验本店最新上线的剧本《古木吟》，期待您在享受该剧本唯美动人的剧情时，也能与同行的TA结缘。满足条件的队伍在完成剧本杀后将会获得本店的特殊奖励哦~'] },
        { name: '欢乐时光', value: [113.860022, 22.579876, '金海路松茂御龙湾商业街A120号', '深圳新晋火爆西餐厅', '一男一女', '品尝', '../../../public/huanle.jpeg', '欢乐时光亲子西餐厅是深圳新晋火爆西餐厅，本店菜品丰富，环境干净卫生，氛围温馨浪漫，并提供亲子聚会和轰趴场地服务，更有k歌房、游戏台和台球桌等设施。', '诚挚邀请一位美丽的她与一位帅气的他在这个特别的夜晚于本店共进晚餐，享受本店温馨氛围和美味菜品的同时，也希望本店成为二位故事的开始。今晚共进晚餐的二位将享受本店提供的特别折扣。'] }
      ],
      discountsData: [
        { name: '喜茶', value: [114.067215, 22.5754, '福田区中康路卓悦汇商场L01楼L1-36号', '世界上最好喝的奶茶之一', '一男一女', '品尝', '../../../public/xicha.jpg', '2012年，原名皇茶ROYALTEA。为了与层出不穷的山寨品牌区分开来，故全面升级为注册品牌喜茶HEYTEA。喜茶为芝士现泡茶的原创者。自创立以来，喜茶专注于呈现来自世界各地的优质茶香，让茶饮这一古老文化焕发出新的生命力。现在，喜茶仍是最受欢迎的饮料品牌之一。', '本店诚挚邀请一对有缘男女一同品尝当季水果限定系列中最新上线的“生打椰椰奶冻”和“生打椰椰芒”，协助我店新品能更好地适应两性口味的共同喜好。参与者将有机会获得本店的饮品特惠哦~'] },
        { name: '英嘉尼私人影院', value: [114.133347, 22.636597, '龙岗区布澜路联创科技园二期', '龙岗私人影院排名第三', '一男一女', '观影', '../../../public/dianyingyuan.jpeg', '英嘉尼影院研发团队注重声音的每一个细节，兼顾高清3D游戏，以“智能影院，唱享未来”的设计理念，化繁为简，从科技感的外观设计，高品质的音效追求，一体化的功能，便捷的安装，简易的操作，满足现代家庭娱乐生活的的高品质需求，匠心打造出了一系列优质家庭影院产品。', '英嘉尼影院诚挚邀请两位有缘的他与她一同观看最新上线电影《信条》，在拥有最优质的观影体验的同时，也希望优秀的电影也能带你走近优秀的TA。本次两位参与者将有机会获得影院特别准备的电影周边产品。'] }
      ],
      chart: '',
      option: ''
    }
  },
  mounted() {
    this.getData()

    this.drawTempMap()
    // console.log(this.option)
    window.addEventListener(
      'resize',
      () => {
        this.$refs.map.resize()
      },
      false
    )
  },
  methods: {
    getData() {
      this.axios
        .post('/get_task_on_map', {
          user_id: 'admin'
        })
        .then((res) => {
          this.freeData = res.data["freeData"]

        })
        .catch((error) => {
          alert(error)
        })
    },
    drawTempMap() {
      this.chart = echarts.init(document.getElementById('temp-chart'))

      // 创建地图实例
      // var map = new BMap.Map("temp-chart");

      this.chart.setOption({
        bmap: {
          center: [114.062992, 22.63222],
          zoom: 12,
          // backgroundColor: '#404a59',
          roam: false,
          mapStyle: {
            // styleJson: mapConfig
          }
          // 百度地图的自定义样式，见 http://developer.baidu.com/map/jsdevelop-11.htm
        },

        tooltip: {
          show: true,
          trigger: 'item',
          formatter: function(obj) {
            var value = obj.value
            return '<div style="border-bottom: 1px solid rgba(255,255,255,.3); font-size: 18px;padding-bottom: 7px;margin-bottom: 7px; font-family: \'jdjszhong\'">' + obj.name + ': ' + obj.seriesName + '</div>' + '<div style="text-align: left; font-family: \'jdjszhong\'">' + '地址: ' + value[2] + '<br>' + '简介: ' + value[3] + '<br>' + '邀请: ' + value[4] + '<br>' + '形式: ' + value[5] + '</div>'
          }
        },
        series: [
          {
            name: 'FREE',
            type: 'effectScatter',
            coordinateSystem: 'bmap',
            /* data: [
              [114.218297, 22.692285], // CUHKSZ
              [113.950382, 22.546199], // Ju Ben Sha
              [113.979399, 22.540746] // SHi jie zhi chuang
            ],*/
            data: this.freeData,
            encode: {
              value: 2
            },
            label: {
              formatter: '{b}',
              position: 'right'
            },
            itemStyle: {
              color: '#800080'
            },
            symbolSize: 25,
            emphasis: {
              label: {
                // show: true
              }
            }
          },
          {
            name: '90% OFF',
            type: 'effectScatter',
            coordinateSystem: 'bmap',
            data: this.discountsData,
            encode: {
              value: 2
            },
            label: {
              formatter: '{b}',
              position: 'right'
            },
            symbolSize: 15,
            emphasis: {
              label: {
                // show: true
              }
            }
          }
        ]
      })
      // var map = this.chart.getModel().getComponent('bmap').getBMap
      // map.setMinZoom(6)
      // map.setMaxZoom(60)
      this.chart.on('click', data => {
        // console.log(data)
        // window.location.href = 'http://localhost:9528/#/employer/1'
        var free_length = this.freeData.length
        var discounts_length = this.discountsData.length
        if (data.seriesName === 'FREE') {
          for (var idx = 0; idx < free_length; idx++) {
            if (this.freeData[idx].name === data.name) var give_data = this.freeData[idx]
          }
        } else if (data.seriesName === '90% OFF') {
          for (var idx = 0; idx < discounts_length; idx++) {
            if (this.discountsData[idx].name === data.name) var give_data = this.discountsData[idx]
          }
        }
        this.$router.push({
          path: '/employer/1',
          query: {
            site: give_data
          }
        })
      })
    }
  }
}
</script>

<style scoped>
.bg-box {
  border-radius: 4%;
  border-width: 10px;
  box-shadow: 0px 0px 5px #00C957;
  /* background-color: white; */
  box-sizing: border-box;
  /* text-align: center; */
}
.temp-chart {
  width: 90%;
  height: 800px;
  text-align: center;
  margin: 0 auto;
}
</style>


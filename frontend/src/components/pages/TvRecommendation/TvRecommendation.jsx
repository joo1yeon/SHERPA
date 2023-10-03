import React, { useState, useLayoutEffect, useEffect } from "react";
import { useSelector } from "react-redux";
import axios from "axios";
import RecommendTarget from "../../organisms/RecommendTarget";
import OfflineMediaRecommendation from "../../organisms/OfflineMediaRecommendation";
import ChannelRecommendation from "../../organisms/ChannelRecommendation";
import TimeRecommendation from "../../organisms/TimeRecommendation";
import ProducerRecommendation from "../../organisms/ProducerCardList";
import {
  Container,
  TargetBox,
  Box,
  Hr,
  ProducerTitleItem,
  SaveBox,
  ButtonBox,
} from "./TvRecommendation";
import Button from "../../atoms/Button";
import { useNavigate } from "react-router-dom";

const APPLICATION_FAST_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8000";

const APPLICATION_SPRING_SERVER_URL =
  process.env.NODE_ENV === "production"
    ? "https://j9c107.p.ssafy.io"
    : "http://j9c107.p.ssafy.io:8080";

export const TvRecommendation = () => {
  const navigate = useNavigate();
  const name = useSelector((state) => state.user.name);
  const targetCheck = useSelector((state) => state.result.target);
  console.log("전역 target", targetCheck);
  const ageDatas = useSelector((state) => state.result.target.age);
  console.log("ageDages 뭉탱이", ageDatas);
  const [ages, setAges] = useState([]);
  useLayoutEffect(() => {
    const newAges = [];
    for (let i = 0; i < ageDatas.length; i++) {
      if (ageDatas[i]) {
        newAges.push(ageDatas[i].value);
      } else {
        newAges.push(0);
      }
    }
    setAges(newAges);
  }, [ageDatas]);
  const male = useSelector((state) => state.result.target.gender[1].value);
  const female = useSelector((state) => state.result.target.gender[0].value);
  const gender = useSelector((state) => state.result.target.recommend.gender);
  const age = useSelector((state) => state.result.target.recommend.age);
  const mainList = useSelector((state) => state.result.media);
  console.log("메인 매체 결과", mainList);
  const mediaList = useSelector((state) => state.result.media.totalList);
  const [mediaLabels, setMediaLabels] = useState([]);
  const [mainDatas, setMainDatas] = useState([]);
  useLayoutEffect(() => {
    const mediaLabels = [];
    const mainDatas = [];
    for (let i = 0; i < mediaList.length; i++) {
      if (mediaList[i]) {
        mediaLabels.push(mediaList[i].name);
        mainDatas.push(mediaList[i].value);
      } else {
        mediaLabels.push(0);
        mainDatas.push(0);
      }
    }
    setMediaLabels(mediaLabels);
    setMainDatas(mainDatas);
  }, [mediaList]);
  const recommendedMedia = useSelector((state) => state.result.media.recommend);
  let target = "성별";
  if (gender === false) {
    target = "남성";
  } else {
    target = "여성";
  }
  const [subMediaLabels, setSubMediaLabels] = useState([]);
  const [subDatas, setSubDatas] = useState([]);
  const [priceLabels, setPriceLabels] = useState([]);
  const [prices, setPrices] = useState([]);
  const [recommendedTvChennl, setRecommendedTvChennl] = useState("");
  const [tvLabels, setTvLabels] = useState([]);
  const [tvChannelDatas, setTvChannelDatas] = useState([]);
  const [recommendedtime, setRecommendedtime] = useState("");
  const [weekdaysDatas, setWeekdaysDatas] = useState([]);
  const [weekendsDatas, setWeekendsDatas] = useState([]);
  const [producerCardDatas, setProducerCardDatas] = useState({});
  const [showProducer, setShowProducer] = useState(false);
  const item = useSelector((state) => state.user.productSmall);
  const sido = useSelector((state) => state.result.selectedBigRegion);
  const sigunguId = useSelector((state) => state.result.selectedSmallRegion);
  const selectedPrice = useSelector((state) => state.result.selectedPrice);
  const onOff = useSelector((state) => state.result.selectedOnOffline);

  useLayoutEffect(() => {
    console.log(`NODE_ENV = ${process.env.NODE_ENV}`);
    console.log(APPLICATION_FAST_SERVER_URL);
    const recommendMedia = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/product`,
          {
            productSmallId: item,
            sigunguId: sigunguId,
            gender: gender,
            age: age,
          }
        );
        console.log("추천 매체 가져오기", response);
        const subMediaLabels = [];
        for (let i = 0; i < response.data.data.mediaList.length; i++) {
          if (response.data.data.mediaList[i]) {
            subMediaLabels.push(response.data.data.mediaList[i].name);
          } else {
            subMediaLabels.push(0);
          }
          setSubMediaLabels(subMediaLabels);
        }
        const subDatas = [];
        for (let i = 0; i < response.data.data.mediaList.length; i++) {
          if (response.data.data.mediaList[i]) {
            subDatas.push(response.data.data.mediaList[i].value);
          } else {
            subDatas.push(0);
          }
          setSubDatas(subDatas);
        }
      } catch (error) {
        console.error("추천 매체 가져오기 오류:", error);
      }
    };
    const recommendPrice = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/budget`,
          {
            budget: selectedPrice,
          }
        );
        console.log("추천 가격 가져오기", response);
        const priceLabels = [];
        for (let i = 0; i < response.data.data.budgetList.length; i++) {
          if (response.data.data.budgetList[i]) {
            priceLabels.push(response.data.data.budgetList[i].name);
          } else {
            priceLabels.push(0);
          }
          setPriceLabels(priceLabels);
        }
        const prices = [];
        for (let i = 0; i < response.data.data.budgetList.length; i++) {
          if (response.data.data.budgetList[i]) {
            prices.push(response.data.data.budgetList[i].value * 0.0001);
          } else {
            prices.push(0);
          }
          setPrices(prices);
        }
      } catch (error) {
        console.error("추천 가격 가져오기 오류:", error);
      }
    };
    const recommendTvChannel = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/tv`,
          {
            gender: {
              0: Number(targetCheck.gender[0].value),
              1: Number(targetCheck.gender[1].value),
            },
            age: {
              10: Number(ageDatas[0].value),
              20: Number(ageDatas[1].value),
              30: Number(ageDatas[2].value),
              40: Number(ageDatas[3].value),
              50: Number(ageDatas[4].value),
              60: Number(ageDatas[5].value),
              70: Number(ageDatas[6].value),
            },
            sidoId: sido,
          }
        );
        console.log("tv채널", response);
        setRecommendedTvChennl(response.data.data.tvList[0].type);
        const tvLabels = [];
        for (let i = 0; i < response.data.data.tvList.length; i++) {
          if (response.data.data.tvList[i]) {
            tvLabels.push(response.data.data.tvList[i].type);
          } else {
            tvLabels.push(0);
          }
        }
        setTvLabels(tvLabels);
        const tvChannelDatas = [];
        for (let i = 0; i < response.data.data.tvList.length; i++) {
          if (response.data.data.tvList[i]) {
            tvChannelDatas.push(response.data.data.tvList[i].ratio);
          } else {
            tvChannelDatas.push(0);
          }
        }
        setTvChannelDatas(tvChannelDatas);
      } catch (error) {
        console.error("tv채널 오류:", error);
      }
    };
    const recommendTime = async () => {
      try {
        const response = await axios.post(
          `${APPLICATION_FAST_SERVER_URL}/fastapi/offline/tv/time`,
          {
            age: {
              10: Number(ageDatas[0].value),
              20: Number(ageDatas[1].value),
              30: Number(ageDatas[2].value),
              40: Number(ageDatas[3].value),
              50: Number(ageDatas[4].value),
              60: Number(ageDatas[5].value),
              70: Number(ageDatas[6].value),
            },
          }
        );
        console.log("tv시간", response);
        setRecommendedtime(response.data.data.weekend_recommend);
        const weekdaysDatas = [];
        for (let i = 0; i < response.data.data.weekdaysDatas.length; i++) {
          if (response.data.data.weekdaysDatas[i]) {
            weekdaysDatas.push(response.data.data.weekdaysDatas[i]);
          } else {
            weekdaysDatas.push(0);
          }
          setWeekdaysDatas(weekdaysDatas);
        }
        const weekendsDatas = [];
        for (let i = 0; i < response.data.data.weekendsDatas.length; i++) {
          if (response.data.data.weekendsDatas[i]) {
            weekendsDatas.push(response.data.data.weekendsDatas[i]);
          } else {
            weekendsDatas.push(0);
          }
          setWeekendsDatas(weekendsDatas);
        }
      } catch (error) {
        console.log("tv시간오류", error);
      }
    };
    const linkproducer = async () => {
      try {
        const response = await axios.get(
          `${APPLICATION_SPRING_SERVER_URL}/api/media/company/3`
        );
        console.log("제작사", response);
        setProducerCardDatas(response.data.data);
      } catch (error) {
        console.log("제작사 오류", error);
      }
    };
    recommendMedia();
    recommendPrice();
    recommendTvChannel();
    recommendTime();
    linkproducer();
  }, []);

  useEffect(() => {
    const delayProducerRender = setTimeout(() => {
      setShowProducer(true);
    }, 2000);
    return () => clearTimeout(delayProducerRender);
  }, []);

  const save = async () => {
    try {
      const response = await axios.post(
        `${APPLICATION_SPRING_SERVER_URL}/api/mypage/save/mediaRec`,
        {
          memberName: name,
          productSmallId: item,
          budget: selectedPrice,
          inOnOff: onOff,
          sigunguId: sigunguId,
          mediaTypeId: 3,
        }
      );
      console.log("저장 성공", response);
    } catch (error) {
      console.log("저장 오류", error);
    }
  };

  return (
    <Container>
      <TargetBox>
        <RecommendTarget
          datas={ages}
          target={target}
          age={age}
          male={male}
          female={female}
        ></RecommendTarget>
      </TargetBox>
      <Hr />
      <Box>
        <OfflineMediaRecommendation
          mediaLabels={mediaLabels}
          subMediaLabels={subMediaLabels}
          priceLabels={priceLabels}
          mainDatas={mainDatas}
          subDatas={subDatas}
          prices={prices}
          recommendedMedia={recommendedMedia}
        ></OfflineMediaRecommendation>
      </Box>
      <Hr />
      <Box>
        <ChannelRecommendation
          title={`추천 드리는 TV 채널은 ${recommendedTvChennl} 입니다.`}
          datas={tvChannelDatas}
          labels={tvLabels}
          description={`${age}대 ${target}이 시청하는 TV 프로그램 통계`}
        ></ChannelRecommendation>
      </Box>
      <Hr />
      <Box>
        <TimeRecommendation
          weekdaysDatas={weekdaysDatas}
          weekendsDatas={weekendsDatas}
          description={`${age}대 ${target}이 TV를 시청하는 시간대 데이터`}
          recommendedtime={recommendedtime}
        ></TimeRecommendation>
      </Box>
      <Hr />
      <Box>
        <ProducerTitleItem>TV 광고 제작사</ProducerTitleItem>
        {showProducer && (
          <ProducerRecommendation cardDatas={producerCardDatas} />
        )}
      </Box>
      <ButtonBox>
        <SaveBox>
          <Button
            backgroundColor="white"
            width="350px"
            height="80px"
            border="1px solid #3C486B"
            textColor="#3C486B"
            fontSize="24px"
            onClick={() => {
              save();
              navigate("/mypage");
            }}
          >
            보관함에 추가
          </Button>
          <Button
            backgroundColor="white"
            width="350px"
            height="80px"
            border="1px solid #3C486B"
            textColor="#3C486B"
            fontSize="24px"
          >
            PDF로 저장
          </Button>
        </SaveBox>
        <Button
          backgroundColor="#3C486B"
          width="890px"
          height="80px"
          textColor="white"
          fontSize="24px"
          onClick={() => {
            navigate("/mediaRecommend");
          }}
        >
          다시 추천받기
        </Button>
      </ButtonBox>
    </Container>
  );
};
export default TvRecommendation;

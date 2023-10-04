import React, { useEffect, useState } from "react";
import styled from "styled-components";
import Chip from '@mui/material/Chip';
import ClearIcon from '@mui/icons-material/Clear';
import { Box, Modal, Typography } from "@mui/material";
import CancelIcon from '@mui/icons-material/Cancel';
import Button from './Button';
import { useSelector } from "react-redux";
import axios from "axios";

const Container = styled.div`
  border: 1px solid #b5b5b5;
  border-radius: 5px;
  padding: 20px;
  width: 315px;
  height: 250px;
  text-align: left;
`;
const TitleBox = styled.div`
  font-size: 24px;
  margin-top: 15px;
  margin-bottom: 30px;
  height: 100px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
`;

const DateBox = styled.div`
  color: #3C486B;
  `
const ChipBox = styled.div`
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
`
const UrlBox = styled.div`
  text-align: right;
`;
const UrlItem = styled.button`
  background-color: white;
  border: 1px solid white;
  color: #3C486B;
  text-decoration: none;
  font-size: 16px;
`;

const IconContainer = styled.div`
  display: flex;
  justify-content: space-between;
`

const FormBox = styled.div`
  display: flex;
  align-items:center;
  justify-content: center;
  flex-direction: column;
  text-align: left;
  padding: 10px;
`

const PhraseBox = styled.div`
  border: 1px solid #DBDBDB;
  border-radius: 4px;
  display: flex;
  align-items:center;
  justify-content: center;
  margin-top: 20px;
  margin-bottom: 10px;

`
const Phrase = styled.div`
  padding: 30px;
`

const CancelBox = styled.div`
  padding-right: 15px;
`

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 1000,
  height: 600,
  bgcolor: 'background.paper',
  border: '1px solid #fff',
  borderRadius: 1,
  p: 4,
  padding: 7,
};


function ContentCardB({date, label, key2, keywordList, mediaTypeId}) {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  const name = useSelector((state) => state.user.name);
  const [scnList, setScnList] = useState([]);

  const APPLICATION_SERVER_URL = 'https://j9c107.p.ssafy.io';

  useEffect(() => {
    const getScn = async () => {
      try {
        const response = await axios.get(APPLICATION_SERVER_URL + `/api/mypage/content/rec/${name}/${key2}`);
        // if (response.data.success) {
        //   console.log(response.data);
        // // }
        // console.log("데이터",response.data.data[0].contentList);
        // console.log("데이터 행렬", response.data.data);
        setScnList(response.data.data[0].contentList);
      } catch (error) {
        console.log('Error!!', error);
      }
    };
    getScn();
  }, [scnList]);

  const deleteScn = (id) => async (e) => {
    e.preventDefault();
    // console.log(id)
    const url = APPLICATION_SERVER_URL +"/api/mypage/content/like/" + name +  "/" + id;
    try {
      const response = await axios.delete(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      console.log("삭제 성공", response)
      alert("삭제 성공하였습니다.")
    } catch (error) {
      console.error("에러메시지 :", error);
      return "실패";
    }
  }

  const deleteSCard = async (e) => {
    e.preventDefault();
    // console.log(key2)
    const url = APPLICATION_SERVER_URL +"/api/mypage/content/rec/" + name +  "/" + key2;
    try {
      const response = await axios.delete(url);
      // console.log("확인 결과 : ", response.data.success);
      // setidConfirm(response.data.success);
      // setIdHelper("사용가능한 닉네임 입니다");
      // console.log(idConfirm);
      // return "성공";
      console.log("삭제 성공", response)
      alert("삭제 성공하였습니다.")
    } catch (error) {
      console.error("에러메시지 :", error);
      return "실패";
    }
  }

  return (
    <Container>
      <IconContainer>
      <DateBox>
        {date.substring(0,4) + "년 " + date.substring(5,7) + "월 " +date.substring(8,10) + "일"}
      </DateBox>
      <ClearIcon onClick={deleteSCard}></ClearIcon>
      </IconContainer>
      <TitleBox>
        {mediaTypeId === 3 ? "TV 광고" : "라디오 광고"}
        <br></br>
        시나리오 추천
      </TitleBox>
      <ChipBox>
      <Chip label={`#${label}`} />
      {keywordList.map(function(a,i){
        return <Chip label={`#${a.keyword}`} color="primary" />
      })}
      {/* <Chip label="#햇빛" color="primary" /> */}
      </ChipBox>
      <UrlBox>
        <UrlItem onClick={handleOpen}>>> 시나리오 보기</UrlItem>
      </UrlBox>

      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style} overflow="auto">
        <Chip label={`#${label}`} />
        {keywordList.map(function(a,i){
          return <Chip label={`#${a.keyword}`} color="primary" />
        })}
          <Typography fontSize={40} align="left">
            시나리오 추천
          </Typography>
          <FormBox>
            {scnList.map(function(a, i){
              return (
            //     <>
            //     <PhraseBox>
            //       <Phrase>
            //         <Typography fontSize={32}>{a.title}</Typography>
            //         <br></br>
            //         <Typography fontSize={24}>{a.content}</Typography>
            //       </Phrase>
            //     </PhraseBox>
                
            // <Button TextColor="white"
            //   width="70px"
            //   height="45px"
            //   border="1px solid #3C486B"
            //   backgroundColor="#3C486B"
            //   fontSize="16px"
            //   onClick = {deleteScn(a.id)}
            // >
            //   삭제
            // </Button>
            // </> 
            <>
              <PhraseBox>
              <Phrase>
                <Typography fontSize={32}>{a.title}</Typography>
                <br></br>
                <Typography fontSize={24}>{a.content}</Typography>
               </Phrase>
                <CancelBox>
                <CancelIcon onClick={deleteScn(a.id)}></CancelIcon>
                </CancelBox>
              </PhraseBox>
              </>
            )
            })}
          </FormBox>
        </Box>
      </Modal>
    </Container>
  );
}

export default ContentCardB;

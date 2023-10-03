package com.ssafy.adrec.myPage.response;

import lombok.Builder;
import lombok.Getter;

import java.time.LocalDateTime;

@Getter
@Builder
public class MediaRecRes {
    Long id;
    LocalDateTime recDate;
    int isOnOff;
    int budget;
    String sigungu;
    String productSmall;
    Long mediaTypeId;
}

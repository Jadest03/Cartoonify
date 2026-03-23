# Cartoonify

OpenCV를 활용하여 일반 실사 사진이나 피규어 이미지를 고품질의 **Cartoon Image**로 변환하는 이미지 프로세싱 툴입니다.   


## Features
1. **K-Means Clustering & Bilateral Filter:** 원본 이미지의 복잡한 색상을 `K=10`으로 군집화하여 셀 애니메이션 특유의 느낌을 만들고, 양방향 필터로 경계를 부드럽게 다듬습니다.
2. **Gaussian Blur Division & Thresholding:**
   원본 흑백 이미지를 가우시안 블러 이미지로 나누는(Divide) 방식을 통해, 조명의 영향을 최소화하고 주변보다 어두운 디테일한 Pencil Sketch만 추출합니다. 이후 Thresholding과 형태학적 닫기(Morphological Closing) 연산을 통해 끊어짐 없는 Ink Sketch을 뽑아냅니다.
3. **Merge:**
   단순화된 색상 이미지 위에 추출된 Ink Sketch를 덮어씌워 최종 카툰 렌더링 이미지를 완성했습니다.

## Demo

### Demo 1 : Good Expression
![Demo](/demo1.png)


### Demo 2 : Bad Expression
![Demo](/demo2.png)


## 한계점과 개선 과정
Adaptive Threshold + Bilateral Filter 조합의 명확한 한계점을 발견하고 이를 극복하기 위해 알고리즘을 개선했습니다.

1. **초기 문제점**  
 Bilateral Filter만 사용할 경우 색상의 경계가 뭉개져 만화 특유의 느낌이 나지 않았습니다. 또한 피사체 얼굴과 몸에 Noise을 다수 생성했었습니다.
2. **개선 과정**
    1. **K-Means:** 수채화 현상을 막기 위해 K-Means(K=10) 색상 양자화를 도입하여 강제적으로 면 분할을 하였습니다.
    2. **Division & Median Blur:** 노이즈를 억제하기 위해 전처리로 `medianBlur`를 적용하고, `GaussianBlur`를 이용한 나눗셈을 사용하여 보다 정교하게 추출하였습니다.
3. **한계점**
    알고리즘을 개선했음에도 입력 이미지의 해상도나 조명 상태에 따라 `threshold` 값이나 K-Means의 `K` 값을 매번 직접 수정해줘야 좋은 결과를 얻을 수 있다는 점이 가장 큰 한계점이라고 생각합니다. 향후 이미지의 밝기 히스토그램을 분석하여 임계값을 자동으로 조절하는(Otsu's Method 등)방식을 도입한다면 이를 개선에 도움이 될 수 있을 것이라 생각합니다.
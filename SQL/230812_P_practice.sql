-- 인기있는 아이스크림
SELECT * FROM FIRST_HALF;

SELECT FLAVOR -- , TOTAL_ORDER
    FROM FIRST_HALF
    ORDER BY TOTAL_ORDER desc, SHIPMENT_ID asc;

-- 카테고리별 상품 개수 구하기
-- 문자열 잘라서 추출
SELECT * FROM PRODUCT;

SELECT CATEGORY
        , count(CATEGORY)
    FROM (
        SELECT substr(product_code,1,2) as CATEGORY
            FROM PRODUCT
        ) AS A
    GROUP BY CATEGORY
    ORDER BY CATEGORY;


-- 있었는데요 없었습니다
-- SELECT ANIMAL_ID, NAME
-- FROM (
--     SELECT I.ANIMAL_ID, I.NAME, I.DATETIME AS ID, O.DATETIME AS OD
--         , datediff(I.DATETIME, O.DATETIME) AS DATE
--     FROM ANIMAL_INS AS I
--     LEFT JOIN ANIMAL_OUTS AS O
--     ON I.ANIMAL_ID = O.ANIMAL_ID
--     HAVING DATE > 0
--     ORDER BY I.DATETIME
-- ) AS A;

SELECT I.ANIMAL_ID, I.NAME
    FROM ANIMAL_INS AS I
    INNER JOIN ANIMAL_OUTS AS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
    WHERE I.DATETIME > O.DATETIME
    ORDER BY I.DATETIME;
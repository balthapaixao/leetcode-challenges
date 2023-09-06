SELECT
    h.hacker_id
    , h.name
FROM
    submissions AS s
INNER JOIN challenges AS c
    ON s.challenge_id=c.challenge_id
INNER JOIN difficulty AS d
    ON (c.difficulty_level=d.difficulty_level AND
        s.score=d.score)
INNER JOIN hackers AS h
    ON s.hacker_id=h.hacker_id
GROUP BY
    h.hacker_id
    , h.name
HAVING
    COUNT(s.challenge_id)>1
ORDER BY
    COUNT(s.challenge_id) DESC
    , h.hacker_id ASC
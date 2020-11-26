BEGIN;

--
-- PostgreSQL database dump
--

-- Dumped from database version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.14 (Ubuntu 10.14-0ubuntu0.18.04.1)

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';



--
-- Name: exercise_injury; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.exercise_injury (
    exinj_id integer NOT NULL,
    inj_type_id integer,
    exercise_id integer
);


ALTER TABLE public.exercise_injury OWNER TO vagrant;

--
-- Name: exercise_injury_exinj_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.exercise_injury_exinj_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercise_injury_exinj_id_seq OWNER TO vagrant;

--
-- Name: exercise_injury_exinj_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.exercise_injury_exinj_id_seq OWNED BY public.exercise_injury.exinj_id;


--
-- Name: exercise_routine; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.exercise_routine (
    exroutine_id integer NOT NULL,
    routine_id integer,
    exercise_id integer,
    exercise_reps integer
);


ALTER TABLE public.exercise_routine OWNER TO vagrant;

--
-- Name: exercise_routine_exroutine_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.exercise_routine_exroutine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercise_routine_exroutine_id_seq OWNER TO vagrant;

--
-- Name: exercise_routine_exroutine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.exercise_routine_exroutine_id_seq OWNED BY public.exercise_routine.exroutine_id;


--
-- Name: exercises; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.exercises (
    exercise_id integer NOT NULL,
    name character varying NOT NULL,
    description text NOT NULL,
    duration integer NOT NULL,
    equip_req boolean NOT NULL,
    freq integer,
    max_reps integer NOT NULL,
    img character varying
);


ALTER TABLE public.exercises OWNER TO vagrant;

--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.exercises_exercise_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_exercise_id_seq OWNER TO vagrant;

--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.exercises_exercise_id_seq OWNED BY public.exercises.exercise_id;


--
-- Name: injury_types; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.injury_types (
    inj_type_id integer NOT NULL,
    name character varying NOT NULL,
    location character varying NOT NULL
);


ALTER TABLE public.injury_types OWNER TO vagrant;

--
-- Name: injury_types_inj_type_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.injury_types_inj_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.injury_types_inj_type_id_seq OWNER TO vagrant;

--
-- Name: injury_types_inj_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.injury_types_inj_type_id_seq OWNED BY public.injury_types.inj_type_id;


--
-- Name: routines; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.routines (
    routine_id integer NOT NULL,
    user_id integer,
    duration integer,
    date_created timestamp without time zone NOT NULL
);


ALTER TABLE public.routines OWNER TO vagrant;

--
-- Name: routines_routine_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.routines_routine_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.routines_routine_id_seq OWNER TO vagrant;

--
-- Name: routines_routine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.routines_routine_id_seq OWNED BY public.routines.routine_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO vagrant;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: exercise_injury exinj_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_injury ALTER COLUMN exinj_id SET DEFAULT nextval('public.exercise_injury_exinj_id_seq'::regclass);


--
-- Name: exercise_routine exroutine_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_routine ALTER COLUMN exroutine_id SET DEFAULT nextval('public.exercise_routine_exroutine_id_seq'::regclass);


--
-- Name: exercises exercise_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercises ALTER COLUMN exercise_id SET DEFAULT nextval('public.exercises_exercise_id_seq'::regclass);


--
-- Name: injury_types inj_type_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.injury_types ALTER COLUMN inj_type_id SET DEFAULT nextval('public.injury_types_inj_type_id_seq'::regclass);


--
-- Name: routines routine_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.routines ALTER COLUMN routine_id SET DEFAULT nextval('public.routines_routine_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: exercise_injury; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.exercise_injury (exinj_id, inj_type_id, exercise_id) FROM stdin;
1	1	1
2	1	2
3	1	3
4	1	4
5	2	5
6	2	6
7	2	7
8	2	8
9	3	2
10	3	4
11	3	6
12	3	8
13	1	5
14	1	6
15	1	7
16	1	8
17	1	9
18	1	10
\.


--
-- Data for Name: exercise_routine; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.exercise_routine (exroutine_id, routine_id, exercise_id, exercise_reps) FROM stdin;
1	1	1	\N
2	2	2	\N
3	3	2	\N
4	6	5	\N
5	7	7	100
6	7	8	66
7	7	9	33
8	8	5	66
9	8	2	40
10	8	7	100
11	9	3	200
12	10	10	2
13	10	4	30
14	10	9	25
15	10	3	50
16	11	2	30
17	11	8	50
18	11	7	75
19	11	9	25
20	14	5	50
21	14	7	75
22	14	9	25
23	14	3	50
24	15	8	50
25	15	7	75
\.


--
-- Data for Name: exercises; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.exercises (exercise_id, name, description, duration, equip_req, freq, max_reps, img) FROM stdin;
1	Crab Walk	With knees bent, step one foot out to the side, then bring the other foot to it. Continuing walking sideways like this for 20 steps, then switch sides.	4	f	3	20	\N
2	Ankle Flex with Resistance Band	With one end of the resistance band looped around the ball of the foot, and the other held in place by your hand, or tied to a stable object, pull against the band using your ankle. Hold for 3 seconds, then release.	5	t	7	20	\N
3	Ankle Circles	Slowly rotate your ankle clockwise. Repate counterclockwise.	3	f	7	20	\N
4	Squats (supported)	Stand with feet shoulder-width apart, in front of a stable support for balance if needed. Slowly bend your knees and lower your body toward the floor. Your body weight should be mostly directed your the heels of your feet. Return to standing.	5	f	3	10	\N
5	Step Up	Start by standing in front of a step/step stool with both feet on the ground. Step up the step with one leg and then with the other. Return to starting position by taking a step back toward the floor leading with the same leg you started with.	3	t	4	20	\N
6	Standing Heel Raises	Stand in front of a counter or other surface at about waist height. Rise up on your toes and lift your heels off the ground. Start with lifting only a couple inches off the ground, then progress, as strength allows. Lower back to the floor slowly. Start by shifting weight onto uninjured foot, then shift to even weight distribution once you've reached the top of the lift. Try to stay even as you lower back down.	1	f	7	20	\N
7	Walking	Concentrate on form, rather than endurance or speed. Focus on making sure strides are even in length, and roll all the way through your injured foot if possible (stead of limping). Take it slow, take shorter strides to start.	2	f	7	30	\N
8	Arch Lifts	Start with both feet on the floor. While pressing your toes and heels into the floor, try to peel the arch of your foot off the floor. Hold for 2 seconds, release slowly.	3	f	7	15	\N
9	Toe Yoga	Sit with knees over ankles. Keep ball and heel of the foot on the floor at all times. Lift the big toe, presisng the other toes into the floor. Hold for 5 seconds. Alternate by pressing the big toes into the floor, while lifting all other toes and hold for 5 seconds.	6	f	7	20	\N
10	Seated Calf Stretch	While sitting, use a towel or other strap (without stretch) looped around the base of your foot. Gently pull the towel taut, and press against it with your foot. You should feel a stretch along the back of your leg. Attempt to straighten your knee for added stretch, if it's comfortable. Hold for 1 minute.	60	t	7	1	\N
\.


--
-- Data for Name: injury_types; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.injury_types (inj_type_id, name, location) FROM stdin;
1	Trimalleolar fracture	ankle
2	Torn meniscus	knee
3	Carpal tunnel	wrist
\.


--
-- Data for Name: routines; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.routines (routine_id, user_id, duration, date_created) FROM stdin;
1	1	10	2020-11-23 05:58:26.214721
2	1	20	2020-11-23 05:58:26.214888
3	1	5	2020-11-23 05:58:26.214961
4	1	10	2020-11-23 22:20:00.457615
5	1	10	2020-11-23 22:35:04.478747
6	1	10	2020-11-23 22:35:55.300032
7	1	10	2020-11-23 22:37:04.346365
8	1	10	2020-11-23 22:38:56.668551
9	1	10	2020-11-25 02:28:42.239671
10	1	10	2020-11-25 02:30:57.614426
11	1	10	2020-11-25 02:47:45.264048
12	1	10	2020-11-25 03:19:18.194342
13	1	10	2020-11-25 03:22:47.174545
14	1	10	2020-11-25 03:32:53.326372
15	1	5	2020-11-25 03:32:53.326372
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (user_id, email, password) FROM stdin;
1	loranne.n@gmail.com	1234007
2	l.orannen@gmail.com	1234007
\.


--
-- Name: exercise_injury_exinj_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--


--
-- Name: exercise_routine_exroutine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--



--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--



--
-- Name: injury_types_inj_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--



--
-- Name: routines_routine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--



--
-- Name: exercise_injury exercise_injury_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_injury
    ADD CONSTRAINT exercise_injury_pkey PRIMARY KEY (exinj_id);


--
-- Name: exercise_routine exercise_routine_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_routine
    ADD CONSTRAINT exercise_routine_pkey PRIMARY KEY (exroutine_id);


--
-- Name: exercises exercises_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_name_key UNIQUE (name);


--
-- Name: exercises exercises_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercises
    ADD CONSTRAINT exercises_pkey PRIMARY KEY (exercise_id);


--
-- Name: injury_types injury_types_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.injury_types
    ADD CONSTRAINT injury_types_pkey PRIMARY KEY (inj_type_id);


--
-- Name: routines routines_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.routines
    ADD CONSTRAINT routines_pkey PRIMARY KEY (routine_id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: exercise_injury exercise_injury_exercise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_injury
    ADD CONSTRAINT exercise_injury_exercise_id_fkey FOREIGN KEY (exercise_id) REFERENCES public.exercises(exercise_id);


--
-- Name: exercise_injury exercise_injury_inj_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_injury
    ADD CONSTRAINT exercise_injury_inj_type_id_fkey FOREIGN KEY (inj_type_id) REFERENCES public.injury_types(inj_type_id);


--
-- Name: exercise_routine exercise_routine_exercise_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_routine
    ADD CONSTRAINT exercise_routine_exercise_id_fkey FOREIGN KEY (exercise_id) REFERENCES public.exercises(exercise_id);


--
-- Name: exercise_routine exercise_routine_routine_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.exercise_routine
    ADD CONSTRAINT exercise_routine_routine_id_fkey FOREIGN KEY (routine_id) REFERENCES public.routines(routine_id);


--
-- Name: routines routines_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.routines
    ADD CONSTRAINT routines_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

END;
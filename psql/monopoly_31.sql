PGDMP  (    8            	    |            monopoly_31    17.0    17.0     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16388    monopoly_31    DATABASE        CREATE DATABASE monopoly_31 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Russia.1251';
    DROP DATABASE monopoly_31;
                     postgres    false            �           0    0    DATABASE monopoly_31    COMMENT     6   COMMENT ON DATABASE monopoly_31 IS 'online monopoly';
                        postgres    false    4796                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                     pg_database_owner    false            �           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                        pg_database_owner    false    4            �            1259    16390    player    TABLE     �   CREATE TABLE public.player (
    id integer NOT NULL,
    name character varying(30),
    password character varying(30),
    email character varying(50)
);
    DROP TABLE public.player;
       public         heap r       postgres    false    4            �            1259    16389    player_id_seq    SEQUENCE     �   CREATE SEQUENCE public.player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.player_id_seq;
       public               postgres    false    4    218            �           0    0    player_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public.player_id_seq OWNED BY public.player.id;
          public               postgres    false    217            !           2604    16393 	   player id    DEFAULT     f   ALTER TABLE ONLY public.player ALTER COLUMN id SET DEFAULT nextval('public.player_id_seq'::regclass);
 8   ALTER TABLE public.player ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            �          0    16390    player 
   TABLE DATA           ;   COPY public.player (id, name, password, email) FROM stdin;
    public               postgres    false    218          �           0    0    player_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.player_id_seq', 4, true);
          public               postgres    false    217            #           2606    16395    player player_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (id);
 <   ALTER TABLE ONLY public.player DROP CONSTRAINT player_pkey;
       public                 postgres    false    218            �   �   x�%�=�0����aJ�qp̠SA;9� ��h^䚢駷�����p�,)CKZh��r%�kD3xbW=�W�,��$��&�Vɬ4\���b)��Ő�=�&Sx��M���GN��?�����2;&#��
�V)�~N,7     